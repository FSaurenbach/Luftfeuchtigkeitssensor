import time
import board
import adafruit_dht
from datetime import datetime

sensor1 = adafruit_dht.DHT11(board.D23)
sensor2 = adafruit_dht.DHT11(board.D24)

def should_read_data():
    """Check if it's time to read data."""
    now = datetime.now()
    current_minute = now.strftime("%M")
    if "0" in current_minute or "5" in current_minute:
        print("It is time")
        return True
    else:
        return False

def write_data_to_file(filename, data):
    """Write data to a file with a timestamp."""
    with open(filename, "a") as f:
        now = datetime.now()
        current_minute = now.strftime("%H:%M")
        f.write(current_minute + "," + data + "\n")

while True:
    if should_read_data():
        try:
            humidity1, temperature1 = sensor1.humidity, sensor1.temperature
            humidity2, temperature2 = sensor2.humidity, sensor2.temperature
            print(" Humidity Sensor1: {}% ".format(humidity1))
            print(" Temperature Sensor1: {} ".format(temperature1))
            print(" Humidity Sensor2: {}% ".format(humidity2))
            print(" Temperature Sensor2: {} ".format(temperature2))
            write_data_to_file("Temperatur.txt", "{},{}".format(temperature1, temperature2))
            write_data_to_file("Luftfeuchtigkeit.txt", "{},{}".format(humidity1, humidity2))

        except (RuntimeError) as error:
            print(error)
            time.sleep(2)
            continue

    remaining_time = 300 - int(time.time() % 300)  # 300 seconds = 5 minutes
    time.sleep(remaining_time)
