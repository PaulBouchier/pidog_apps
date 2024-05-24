from pidog import Pidog
import time

my_dog = Pidog()
sum_x = 0

while True:
    gx, gy, gz = my_dog.gyroData
    sum_x += gx
    print(f"gyroData: {gx} °/s, {gy} °/s, {gz} °/s, {sum_x} deg u\xb0")
    time.sleep(0.2)

my_dog.close()