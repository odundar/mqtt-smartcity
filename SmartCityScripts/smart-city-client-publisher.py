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
import asyncio
import datetime
import ssl

from sensor_simulator import SensorSim

class ClientConfig():
    '''
    Client Connection Configurations
    '''
    SystemName = "hypo_city"

    # city id and street name
    CityName = "city_01"
    StreetName = "street_01"

    def GetClientId(self):
        return self.CityName + "_" + self.StreetName

    # define the server IP and port to be used
    MQTTServer = "127.0.0.1"
    TSLServerPort = 8883
    ServerPort = 1883

    Username = 'street1'
    Password = 'simple_password'

    QoS = 0
    Retain = False

    def parse_config_file(self, file_name=''):
        """
        A config file can be used to parse data

        :param file_name:
        :return:
        """

        return True

    def topic_prefix(self):
        return self.SystemName + "/" + self.CityName + "/" + self.StreetName

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))

def on_publish(client, userdata, result):
    print("Message Published {}".format(result))


async def publish_message(mqtt_client=mqtt.Client(), topic_prefix='', qos=0, retain=False):
    """

    :param mqtt_client:
    :param topic_prefix:
    :param qos:
    :param retain:
    :return:
    """
    print('{} started'.format(__name__))

    sim = SensorSim()

    sim.start_celcius_temperature(mean=28.7, std_dev=3.5, interval=10)
    sim.start_fahrenheit_temperature(mean=88.3, std_dev=9.5, interval=10)
    sim.start_no2_level(mean=87.3, std_dev=0.5, interval=10)
    sim.start_so2_level(mean=122.1, std_dev=0.5, interval=10)
    sim.start_wind_direction(mean=123.8, std_dev=65.7, interval=10)
    sim.start_wind_speed(mean=15.8, std_dev=8.5, interval=10)
    sim.start_traffic_speed(mean=0.0, std_dev=25, interval=10)

    while True:
        utc_time = datetime.datetime.utcnow()

        # message structure
        # timestampt \t data

        message_f = '{}\t{}'.format(utc_time, sim.fahrenheit)
        message_c = '{}\t{}'.format(utc_time, sim.celcius)
        message_so2 = '{}\t{}'.format(utc_time, sim.so2_level)
        message_no2 = '{}\t{}'.format(utc_time, sim.no2_level)
        message_ws = '{}\t{}'.format(utc_time, sim.wind_speed)
        message_wd = '{}\t{}'.format(utc_time, sim.wind_direction)
        message_ts = '{}\t{}'.format(utc_time, sim.traffic_speed)

        topic = topic_prefix + "/temperature/fahrenheit"
        publish_info = client.publish(topic, payload=message_f, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_f))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/temperature/celcius"
        publish_info = client.publish(topic, payload=message_c, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_c))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/air_pollution/so2_level"
        publish_info = client.publish(topic, payload=message_so2, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_so2))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/air_pollution/no2_level"
        publish_info = client.publish(topic, payload=message_no2, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_no2))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/air_condition/wind_speed"
        publish_info = client.publish(topic, payload=message_ws, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_ws))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/traffic/traffic_speed"
        publish_info = client.publish(topic, payload=message_ts, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_ts))
        else:
            print("Message Not Published")

        topic = topic_prefix + "/air_condition/wind_direction"
        publish_info = client.publish(topic, payload=message_wd, qos=qos, retain=retain)

        if publish_info.is_published:
            print("Topic:{}, Message:{}".format(topic, message_wd))
        else:
            print("Message Not Published")

        await asyncio.sleep(10)


if __name__ == '__main__':
    cfg = ClientConfig()

    if not cfg.parse_config_file():
        exit(-1)

    # Create Client Object and assign publisher callback methods
    client = mqtt.Client(client_id=cfg.GetClientId())

    # assign callback methods
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect

    client.tls_set(ca_certs='../ca.crt', tls_version=ssl.PROTOCOL_TLSv1, cert_reqs=ssl.CERT_REQUIRED)

    # set username password
    client.username_pw_set(ClientConfig.Username, password=ClientConfig.Password)

    # Connect to MQTT Broker
    client.connect(ClientConfig.MQTTServer, ClientConfig.TSLServerPort, keepalive=60)

    loop = asyncio.get_event_loop()
    loop.create_task(publish_message(mqtt_client=client, topic_prefix=cfg.topic_prefix(), qos=cfg.QoS, retain=cfg.Retain))

    if not loop.is_running():
        loop.run_forever()