from pidog import Pidog
from robot_hat import Pin
import time

#forward_count = 46
#backward_count = 43
forward_count = 22
backward_count = 20
#forward_count = 1
#backward_count = 1

my_dog = Pidog()
button_pin = Pin('SW', Pin.IN, Pin.PULL_UP)

try:
    # walk
    my_dog.do_action("stand", speed=60)
    my_dog.wait_all_done()
    my_dog.do_action("forward", step_count=1, speed=90)
    my_dog.wait_all_done()
    print('press button to start')
    while True:
        if button_pin.value():
            print('Starting quicktrip')
            time.sleep(2)
            break
        time.sleep(0.1)
    my_dog.do_action("forward", step_count=forward_count, speed=98)
    my_dog.wait_all_done()
    time.sleep(5)
    my_dog.do_action("stand", speed=60)
    my_dog.wait_all_done()
    time.sleep(2)
    my_dog.do_action("backward", step_count=backward_count, speed=98)
    my_dog.wait_all_done()

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\033[31mERROR: {e}\033[m")
finally:
    print("closing ...")
    my_dog.close()