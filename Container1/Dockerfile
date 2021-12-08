FROM ubuntu:16.04
      
MAINTAINER Radoslaw Lis <radoslaw.lis@mailbox.tu-dresden.de>

RUN useradd -u 1000 Ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y memcached

RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]


# add more stuff here
