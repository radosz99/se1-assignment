FROM ubuntu:16.04
      
MAINTAINER Radoslaw Lis <radoslaw.lis@mailbox.tu-dresden.de>

RUN apt-get update
RUN apt-get -y install sudo

RUN useradd  --create-home -u 1000 ubuntu && echo 'ubuntu:password' | chpasswd
RUN adduser ubuntu sudo
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]


RUN mkdir /home/ubuntu/.ssh
COPY gitlab_id_rsa.pub /home/ubuntu/.ssh/authorized_keys
COPY containers_key.pub /home/ubuntu/.ssh
RUN cat /home/ubuntu/.ssh/containers_key.pub >> /home/ubuntu/.ssh/authorized_keys

# add more stuff here
RUN apt-get install -y memcached
EXPOSE 11222
