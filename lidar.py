from TFmini_I2C import TFminiI2C
import time

Lidar = TFminiI2C(1, 0x10)
while True:
	print("Distancia: ", Lidar.readAll(), " cm.")
	time.sleep(3)
