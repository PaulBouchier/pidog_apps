from pidog import Pidog
import time

# forward_count = 46
# backward_count = 43
forward_count = 5
backward_count = 5

my_dog = Pidog()

try:
    # walk
    my_dog.do_action("stand", speed=60)
    my_dog.wait_all_done()
    time.sleep(5)
    for i in range(2):
        my_dog.do_action("forward", step_count=1, speed=98)
    my_dog.wait_all_done()
    my_dog.do_action("turn_left", step_count=1, speed=98)
    my_dog.wait_all_done()
    for i in range(2):
        my_dog.do_action("forward", step_count=1, speed=98)
    my_dog.wait_all_done()
    time.sleep(5)
    for i in range(backward_count):
        my_dog.do_action("backward", step_count=1, speed=98)
        my_dog.wait_all_done()

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\033[31mERROR: {e}\033[m")
finally:
    print("closing ...")
    my_dog.close()