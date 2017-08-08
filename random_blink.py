from gpiozero import LED
from time import sleep
import random

red_led = LED(17)

while True:
    red_led.on()
    sleep(float(random.randint(0, 5) / 10))
    red_led.off()
    sleep(float(random.randint(0, 5) / 10))
