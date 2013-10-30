from time import sleep
import RPi.GPIO as GPIO

# setup some names references to the LED's and buttons
# site1 red     = pin 13
# site1 amber   = pin 12
# site1 green   = pin 7

# site2 red   = pin 18
# site2 amber = pin 16
# site2 green = pin 15

GPIO.setmode(GPIO.BCM)

#Set up the GPIO pins to be used

leds = [13, 12, 7, 18, 16, 15]
button = 26

#Buzzer setup
GPIO.setup(22,GPIO.OUT)

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED setup
for n in leds
  GPIO.setup(n, GPIO.OUT)
  GPIO.output(n, False)
   
with open("/home/user/pi-nagios-lights/site1/redalertcount") as f:
    data = f.read()
    if f > 0
      while RedAlert:
      GPIO.output(13,GPIO.HIGH)
      
with open("/home/user/pi-nagios-lights/site1/orangealertcount") as f:
    data = f.read()
    if f > 0
      GPIO.output(12,GPIO.HIGH)
      
with open("/home/user/pi-nagios-lights/site1/greenalertcount") as f:
    data = f.read()
    if f > 0
      while GreenAlert:
        GPIO.output(7,GPIO.HIGH)
        sleep(2)  
        GPIO.output(7,GPIO.LOW)

try:  
    GPIO.wait_for_edge(26, GPIO.FALLING)  
    GPIO.output(22, GPIO.LOW)

except KeyboardInterrupt:
  GPIO.cleanup() #clean up GPIO on CTRL-C exit
GPIO.cleanup()   #clean up GPIO on normal exit
