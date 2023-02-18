import time
import board
import adafruit_dht
from datetime import datetime
sensor1 = adafruit_dht.DHT11(board.D23)
sensor2 = adafruit_dht.DHT11(board.D24)

def is_time(): # Alle 5 Minuten die Daten auslesen.
	now = datetime.now()
	current_minute = now.strftime("%M")
	print(current_minute)
	if "0" in current_minute or "5" in current_minute:
		print("It is time")
		return True
	else:
		return False


while True:
	if is_time():
		try:
			humidity1 = sensor1.humidity
			temperature1 = sensor1.temperature
			humidity2 = sensor2.humidity
			temperature2 = sensor2.temperature
			print(" Humidity Sensor1: {}% ".format(humidity1))
			print(" Temperature Sensor1: {} ".format(temperature1))
			print(" Humidity Sensor2: {}% ".format(humidity2))
			print(" Temperature Sensor2: {} ".format(temperature2))
			with open("Temperatur.txt", "a") as f:
				f.write("\n")
				now = datetime.now()
				current_minute = now.strftime("%H:%M")
				f.write(current_minute + " ," + str(temperature1) + "," + str(temperature2))
			with open("Luftfeuchtigkeit.txt", a) as f:
				f.write("\n")
				now = datetime.now()
				current_minute = now.strftime("%H:%M")
				f.write(current_minute + "," + str(humidity1) + "," + str(humidity2))

			time.sleep(120)
		except RuntimeError as error:
			print(error.args[0])
			time.sleep(2)
			continue
	time.sleep(20)
