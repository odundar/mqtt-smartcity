# MIT License
#
# Copyright (c) 2018 Onur
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import paho.mqtt.client as mqtt
import ssl


class ClientConfig():
    '''
    Client Connection Configurations
    '''
    SystemName = "hypo_city"

    def GetClientId(self):
        return 'TemperatureServer'

    #systename/cityname/streetname/sensortype/data
    subs_topic = SystemName + '/+/+/temperature/+'

    def GetSubscribedTopic(self):
        return subscribe_topic

    # define the server IP and port to be used
    MQTTServer = "127.0.0.1"
    TSLServerPort = 8883
    ServerPort = 1883

    Username = 'subscriber1'
    Password = 'simple_password'

    QoS = 0
    Retain = False

    def parse_config_file(self, file_name=''):
        """
        A config file can be used to parse data

        :param file_name:
        :return:
        """
        #TODO:
        return True


# Call back functions

# Define callback functions for Subscriber
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")

    message_data = message.split('\t')
    topic_data = msg.topic.split('/')

    write_message(topic_data, message_data)


def write_message(topic=list(), message=list()):
    if len(topic) > 0 and len(message > 0):
        timestamp_utc = message[0]
        data = message[1]
        print('System: {}\tCity: {}\tStreet: {}\tSensorType: {}\tDataType: {}\tSensorData: {}\tTimeStamp: {}'
              .format(topic[0],
                      topic[1],
                      topic[2],
                      topic[3],
                      topic[4],
                      data,
                      timestamp_utc))


if __name__ == '__main__':
    cfg = ClientConfig()

    if not cfg.parse_config_file():
        exit(-1)

    # Create Client Object and assign publisher callback methods
    client = mqtt.Client(client_id=cfg.GetClientId())

    # assign callback methods
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.tls_set(ca_certs='../ca.crt', tls_version=ssl.PROTOCOL_TLSv1, cert_reqs=ssl.CERT_REQUIRED)

    # set username password
    client.username_pw_set(ClientConfig.Username, password=ClientConfig.Password)

    # Connect to MQTT Broker
    client.connect(ClientConfig.MQTTServer, ClientConfig.TSLServerPort, keepalive=60)

    # I will get, all cities and all cities streets temperature

    subscribe_topic = cfg.GetSubscribedTopic()  # system_name + '/+/+/+/+'

    client.subscribe(subscribe_topic, qos=0)

    client.loop_forever()
