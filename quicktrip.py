from pidog import Pidog
import time

forward_count = 46
backward_count = 43
#forward_count = 1
#backward_count = 1

my_dog = Pidog()

try:
    # walk
    my_dog.do_action("stand", speed=60)
    my_dog.wait_all_done()
    time.sleep(5)
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