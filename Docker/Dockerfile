# Use an official Python runtime as a parent image
FROM ubuntu:xenial

MAINTAINER Onur Dundar <onur.dundar1@gmail.com>

# run update to get latest updates from repositories
RUN apt-get update

# install mosquitto into image
RUN apt-get install -y mosquitto mosquitto-clients

# install openssl
RUN apt-get install -y openssl

# install mariadb
# https://downloads.mariadb.org/mariadb/repositories/#mirror=ulakbim&distro=Ubuntu&distro_release=xenial--ubuntu_xenial&version=10.3

RUN apt-get install -y software-properties-common
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
RUN add-apt-repository 'deb [arch=amd64,arm64,i386,ppc64el] ftp://ftp.ulak.net.tr/pub/MariaDB/repo/10.3/ubuntu xenial main'
RUN apt-get update

# make noninteractive setup to skip root password setup later
RUN DEBIAN_FRONTEND=noninteractive apt install -y mariadb-server

# extra tools installed
EXPOSE 1883
EXPOSE 8883
EXPOSE 3306
# Rest of the configurations should be done carefully, follow README instructions

# build command
#  docker build --tag mqtt_broker:latest .

#ADD start_services.sh /start_services.sh
#RUN chmod 755 /start_services.sh

#CMD ["/bin/bash", "/start_services.sh"]
