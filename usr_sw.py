from robot_hat import Pin
import time

button_pin = Pin('SW', Pin.IN, Pin.PULL_UP)

while True:
    if button_pin.value():
        print('button pushed')
    else:
        print('button released')
    time.sleep(1)            