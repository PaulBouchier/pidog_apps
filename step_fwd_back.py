from pidog import Pidog
from robot_hat import Pin
import time


def howling(my_dog, volume=100):
    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -30]], speed=95)
    my_dog.wait_all_done()

    my_dog.rgb_strip.set_mode('speak', color='cyan', bps=0.6)
    my_dog.do_action('half_sit', speed=80)
    my_dog.head_move([[0, 0, -60]], speed=80)
    my_dog.wait_all_done()
    my_dog.speak('howling', volume)
    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, 10]], speed=70)
    my_dog.wait_all_done()

    my_dog.do_action('sit', speed=60)
    my_dog.head_move([[0, 0, 10]], speed=80)
    my_dog.wait_all_done()

    time.sleep(2.34)
    my_dog.do_action('sit', speed=80)
    my_dog.head_move([[0, 0, -40]], speed=80)
    my_dog.wait_all_done()

my_dog = Pidog()
button_pin = Pin('SW', Pin.IN, Pin.PULL_UP)
#outbound_steps = 46
#return_steps = 43
outbound_steps = 2
return_steps = 2

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
    my_dog.do_action("forward", step_count=outbound_steps, speed=98)
    my_dog.wait_all_done()
    my_dog.do_action("wag_tail", step_count=15, speed=95)
    my_dog.wait_all_done()
    my_dog.do_action("backward", step_count=return_steps, speed=98)
    my_dog.wait_all_done()
    time.sleep(2)

    for i in range(2):
        howling(my_dog)

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\033[31mERROR: {e}\033[m")
finally:
    print("closing ...")
    my_dog.close()
