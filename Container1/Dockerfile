FROM ubuntu:16.04
      
MAINTAINER Radoslaw Lis <radoslaw.lis@mailbox.tu-dresden.de>

# Global configuration
RUN apt-get update
RUN apt-get -y install sudo

# Adding user
RUN useradd --create-home -u 1000 ubuntu &&  echo 'ubuntu:password' | chpasswd
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# SSH server configuration
RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]


# Keys stuff
USER ubuntu
RUN mkdir /home/ubuntu/.ssh
RUN chmod 700 /home/ubuntu/.ssh
WORKDIR /home/ubuntu/.ssh
RUN touch known_hosts
COPY gitlab_id_rsa.pub authorized_keys
RUN sudo chown ubuntu authorized_keys
RUN echo Container2/containers_key.pub > authorized_keys
RUN sudo chmod 600 known_hosts
RUN sudo chmod 644 authorized_keys
USER root

# Memcached configuration
RUN apt-get install -y memcached
EXPOSE 11222
