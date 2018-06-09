# Use an official Python runtime as a parent image
FROM ubuntu

MAINTAINER Onur Dundar <onur.dundar1@gmail.com>

# run update to get latest updates from repositories
RUN apt-get update

# install mosquitto into image
RUN apt-get install -y mosquitto mosquitto-clients

# Make port 1883 and 9001 available. 
# 1883 is MQTT port
# 9001 is Secure MQTT port to be used
EXPOSE 1883 9001

# how to run this file
# docker build --tag mosquitto_broker --file /PATH/Dockerfile