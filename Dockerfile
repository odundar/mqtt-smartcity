# Use an official Python runtime as a parent image
FROM ubuntu:latest

MAINTAINER Onur Dundar <onur.dundar1@gmail.com>

# run update to get latest updates from repositories
RUN apt-get update

# install mosquitto into image
RUN apt-get install -y mosquitto mosquitto-clients
RUN apt-get install -y openssl

RUN mkdir /etc/mosquitto/passwords/ && touch /etc/mosquitto/passwords/mosquitto_pwd
RUN mosquitto_passwd -U /etc/mosquitto/passwords/mosquitto_pwd
RUN mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd street_publisher simple_password
RUN mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd air_pollution_subscriber simple_password
# or run in commandline with docker attach <container_id>, enter password from command line

RUN cd /etc/mosquitto/ca_certificates
RUN echo 'PASS_PHRASE\nPASS_PHRASE\n' | openssl genrsa -des3 -out ca.key 2048
RUN echo 'PASS_PHRASE\nTR\nCITY\nCMP\nSEC\nTT\nAA\na@a.com\n' | openssl req -new -x509 -days 1826 -key ca.key -out ca.crt
RUN openssl genrsa -out server.key 2048
RUN echo 'TR\nCITY\nCMP\nSEC\nTT\nAA\na@a.com\nPASS_PHRASE\nCMP'openssl req -new -out server.csr -key server.key
RUN echo 'PASS_PHRASE\n' \n openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 360

# get certificate after running mqtt broker
# docker cp <container-id>:/etc/mosquitto/ca_certificates/ca.crt

RUN echo "keyfile /etc/mosquitto/ca_certificates/server.key" >> /etc/mosquitto/mosquitto.conf
RUN echo "certfile /etc/mosquitto/ca_certificates/server.crt" >> /etc/mosquitto/mosquitto.conf
RUN echo "tls_version tlsv1" >> /etc/mosquitto/mosquitto.conf

# Make port 1883 and 9001 available.
# 1883 is MQTT port
# 8883 is Secure MQTT port to be used
EXPOSE 1883 8883

# how to run this to build an image
# docker build --tag "mosquitto:base-image" --file /PATH/Dockerfile

# how to run image inside a container.
# docker run -d -p 1883:1883 -p 8883:8883 mosquitto:base-image

# allow_anonymous true/false

# docker attach <container_id> , go to terminal