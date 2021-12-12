FROM ubuntu:16.04
      
MAINTAINER Radoslaw Lis <radoslaw.lis@mailbox.tu-dresden.de>

# Global configuration
RUN apt-get update
RUN apt-get -y install sudo

# Creating user and setting password
RUN useradd --create-home -u 1000 ubuntu &&  echo 'ubuntu:password' | chpasswd
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Python configuration
RUN apt-get install -y python
RUN apt-get install -y git

# Configuration for ssh server
RUN apt-get install -y openssh-server
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

# Configuration for mcperf
RUN apt install -y gcc
RUN apt-get install -y build-essential
RUN wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz
RUN tar -xvf mcperf-0.1.1.tar.gz mcperf-0.1.1
WORKDIR mcperf-0.1.1
RUN ./configure
RUN make
RUN make install

# Configuration for R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN apt-get install -y software-properties-common
RUN add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
RUN apt-get install -y r-base

# Copy stuff
COPY Container2/ /home/ubuntu
WORKDIR /home/ubuntu
RUN chmod +x run.sh

# Injecting keys
RUN mkdir /home/ubuntu/.ssh
RUN touch /home/ubuntu/.ssh/known_hosts
COPY gitlab_id_rsa.pub /home/ubuntu/.ssh/authorized_keys
COPY containers_key /home/ubuntu/.ssh
RUN chmod 777 /home/ubuntu/.ssh/containers_key
RUN chmod 777 /home/ubuntu/.ssh/known_hosts

# Dude configuration
RUN git clone https://bitbucket.org/db7/dude
WORKDIR dude
RUN sudo python setup.py install --home=/home/ubuntu/local

# For enabling 'dude' execution via non-interactive shell
RUN echo export PATH=$PATH:/home/ubuntu/local/bin >> /etc/environment
RUN echo export PYTHONPATH=/home/ubuntu/local/lib/python >> /etc/environment 


