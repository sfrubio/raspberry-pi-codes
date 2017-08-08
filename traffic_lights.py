from gpiozero import LED
from time import sleep

red_led = LED(22)
yellow_led = LED(27)
green_led = LED(17)
    
while True:
  green_led.on()
  sleep(5)
  green_led.off()
  yellow_led.on()
  sleep(3)
  yellow_led.off()
  red_led.on()
  sleep(10)
  red_led.off()
