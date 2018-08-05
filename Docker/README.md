- Run mqtt_broker image interactively to complete security setup of server to run into its i/o shell.

```commandline
$ docker build --tag mqtt_broker:latest .
$ docker run -ti -p 1883:1883 -p 8883:8883 -p 3306:3306 mqtt_broker:latest
```

### Mosquitto Security Configurations

- Create password file for Mosquitto

```commandline
$ mkdir /etc/mosquitto/passwords/ && touch /etc/mosquitto/passwords/mosquitto_pwd
```

- Change password file from plaintext to hashed version

```commandline
$ mosquitto_passwd -U /etc/mosquitto/passwords/mosquitto_pwd
```

- For each user you want to add to Mosquitto authentication process, you can run following command.
```commandline
$ mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd street1 simple_password
$ mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd street2 simple_password
$ mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd subscriber1 simple_password
$ mosquitto_passwd -b /etc/mosquitto/passwords/mosquitto_pwd subscriber2 simple_password

```

- Edit `/etc/mosquitto/mosquitto.conf` file add following lines.

```commandline
allow_anonymous false
password_file /etc/mosquitto/passwords/mosquitto_pwd
```

If you exit, make sure you commited the container for later use from the last state.

$ docker commit <container_id> mqtt_broker:latest

#### TLS/SSL Configurations for Mosquitto

```commandline
$ cd /etc/mosquitto/ca_certificates
```


- Generate a server key with encrpytion

```commandline
$ openssl genrsa -des3 -out server.key 2048
```

- When prompted, make sure you entered `Common Name` as your host name. In my case, I used localhost as 127.0.0.1 

```commandline
$ openssl req -new -x509 -days 3650 -extensions v3_ca -keyout ca.key -out ca.crt
```

```commandline
$ openssl genrsa -out server.key 2048
```

- Create server key, make sure you entered same `Common Name` (127.0.0.1) as previous one. 

```commandline
$ openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650
```

- Leave files in `certs` folder, and get copy of ca.crt to be used in your client.

Copy ca.crt to your client.

```commandline
$  docker cp <containerid>:/etc/mosquitto/certs/ca.crt <destination folder>
```

Add following lines to /etc/mosquitto/mosquitto.conf file
```commandline
listener 8883

cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key

tls_version tlsv1
```

- Restart service

```commandline
$ service mosquitto restart
```

5. Change allow_anonymous to false

TLS/SSL Configurations for Mosquitto

Now, we will enable SSL connection feature. You can follow following steps. https://mosquitto.org/man/mosquitto-tls-7.html

### MariaDB Configurations

