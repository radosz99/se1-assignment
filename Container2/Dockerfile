FROM ubuntu:16.04
      
MAINTAINER Your name <your.name@mailbox.tu-dresden.de>

RUN useradd --create-home -u 1000 Ubuntu
#RUN echo 'Ubuntu:newpassword' | chpasswd
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

RUN mkdir /home/Ubuntu/.ssh
RUN ln -s /run/secrets/client_ssh_key /home/Ubuntu/.ssh/authorized_keys
