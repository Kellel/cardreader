from msr605.msr605 import MSR605
from time import sleep

r = MSR605('/dev/ttyUSB0', False)

def blink(timeout = 0.5):
    while True:
        r.all_leds_off()
        r.led_green_on()
        sleep(timeout)
        r.led_yellow_on()
        sleep(timeout)
        r.led_red_on()
        sleep(timeout)

if __name__ == "__main__":

    blink()
