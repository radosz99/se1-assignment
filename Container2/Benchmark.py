import os
import stat

def prepare_exp(SSHHost, SSHPort, MEMCACHEDPort, optpt):
    f = open("config", 'w')
    f.write("Host benchmark\n")
    f.write("   Hostname %s\n" % SSHHost)
    f.write("   Port %d\n" % SSHPort)
    f.write("   User ubuntu\n")
    f.write("   IdentityFile /home/ubuntu/.ssh/containers_key\n")
    f.close()
    

    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")

    f.write("ssh -oStrictHostKeyChecking=no -F config benchmark \"nohup memcached -d -p %d > memcached.out 2> memcached.err &\"\n" % MEMCACHEDPort)
    f.write("ssh -F config benchmark \"pidof memcached > memcached.pid\"\n") 
    f.write("RESULT=`ssh -F config benchmark \"pidof memcached\"`\n")

    f.write("sleep 5\n")

    f.write("if [[ -z \"${RESULT// }\" ]]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    f.write("mcperf --linger=0 --conn-rate=%d --call-rate=%d --num-calls=%d --num-conns=%d --sizes=u1,16 --port=%d --server=%s &> stats.log\n\n" % (optpt["connRate"], optpt["callRate"], optpt["numCalls"], optpt["numConns"], MEMCACHEDPort, SSHHost))    

    f.write("REQPERSEC=`grep \"Response rate\" stats.log | grep -Eo '[0-9]+([.][0-9]+)?' | head -1`\n")
    f.write("LATENCY=`grep \"Response time\" stats.log | grep -Eo '[0-9]+([.][0-9]+)?' | head -1`\n")

    f.write("ssh -F config benchmark \"ls\"\n")
    f.write("ssh -F config benchmark \"kill $RESULT\"\n")

    f.write("echo \"requests latency\" > stats.csv\n")
    f.write("echo \"$REQPERSEC $LATENCY\" >> stats.csv\n")
    
    f.write("scp -F config benchmark:~/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()
    
    os.chmod("run-experiment.sh", stat.S_IRWXU) 
