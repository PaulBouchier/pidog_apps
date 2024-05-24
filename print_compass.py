#!/usr/bin/env python3
import time
from robot_hat import I2C

class HMC6352(I2C):
    """
    Class for an HMC6352 digital compass

    Simple functionality -- does not implement anything except getting a heading from the device
    in "standby" mode (see datasheet -- this is the default mode of the device)

    Tested with Python 3.5

    Example usage:

    >>> bus = smbus.SMBus(1)
    >>> compass = HMC6352(0x21, bus)
    >>> print(compass.heading)
    """

    HMC6352_ADDRESS = 0x21
    _READ_CMD = 0x41 # Command is "A"

    def __init__(self):
        """
        Constructor for compass object
        """
        super().__init__(address=self.HMC6352_ADDRESS)
        if not self.is_avaliable():
            raise IOError("HMC6352 is not available")

    @property
    def heading(self):
        """Returns the heading as a double (0.0 - 359.9)"""

        # Read two bytes off the bus once command sent; first byte MSBs, second LSBs
        data = self.mem_read(2, HMC6352._READ_CMD)

        return ((data[0] << 8) + data[1]) / 10


if __name__ == "__main__":
    import time

    print("Testing HMC6352")

    compass = HMC6352()

    while True:
        print(compass.heading)
        time.sleep(0.2)