import asyncio
import numpy as np

class SensorSim(object):
    """
    A Basic Sensor Reading Emulator with Normal Distribution Only
    """

    celcius = 0.0
    cel_running = False

    async def __celcius_temperature__(self, mean=21.5, std_dev=3.5, interval=10):
        cel_running = True
        while cel_running:
            self.celcius = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.cel_running:
            loop.stop()
            loop.close()

    def start_celcius_temperature(self, mean=21.5, std_dev=3.5, interval=10):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__celcius_temperature__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    fahrenheit = 0.0
    fah_running = False

    async def __fahrenheit_temperature__(self, mean=60.5, std_dev=20.5, interval=10):
        fah_running = True

        while fah_running:
            self.fahrenheit = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()

    def start_fahrenheit_temperature(self, mean=60.5, std_dev=20.5, interval=10):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__fahrenheit_temperature__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()

        return True

    wind_speed = 0.0
    ws_running = False

    async def __wind_speed__(self, mean=60.5, std_dev=20.5, interval=10):
        ws_running = True
        while ws_running:
            self.wind_speed = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()


    def start_wind_speed(self, mean=60.5, std_dev=20.5, interval=10):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__wind_speed__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    wind_direction = 0.0
    wd_running = False

    async def __wind_direction__(self, mean=60.5, std_dev=20.5, interval=100):
        wd_running = True
        while wd_running:
            self.wind_direction = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()

    def start_wind_direction(self, mean=0.0, std_dev=180.0, interval=100):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__wind_direction__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    no2_level = 0.0
    no2_running = False

    async def __no2_level__(self, mean=60.5, std_dev=20.5, interval=100):
        no2_running = True
        while no2_running:
            self.no2_level = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()

    def start_no2_level(self, mean=0.0, std_dev=180.0, interval=100):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__no2_level__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    so2_level = 0.0
    so2_running = False

    async def __so2_level__(self, mean=60.5, std_dev=20.5, interval=100):
        so2_running = True

        while so2_running:
            self.so2_level = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()

    def start_so2_level(self, mean=0.0, std_dev=180.0, interval=100):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__so2_level__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    traffic_speed = 0.0
    ts_running = False

    async def __traffic_speed__(self, mean=60.5, std_dev=20.5, interval=10):
        ts_running = True
        while ts_running:
            self.traffic_speed = np.random.normal(loc=mean, scale=std_dev)
            await asyncio.sleep(interval)

        loop = asyncio.get_event_loop()
        if not self.fah_running:
            loop.stop()
            loop.close()

    def start_traffic_speed(self, mean=60.5, std_dev=20.5, interval=10):
        loop = asyncio.get_event_loop()
        loop.create_task(self.__traffic_speed__(mean, std_dev, interval))
        print('{} started'.format(__name__))
        if not loop.is_running():
            loop.run_forever()
        return True

    def __init__(self):
        return None
