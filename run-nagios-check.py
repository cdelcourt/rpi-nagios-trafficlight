#!/usr/bin/python3

# Some references to the LED's

# Row 1 Red		= pin 13
# Row 1 Amber		= pin 12
# Row 1 Green		= pin 7

# Row 2 Red		= pin 18
# Row 2 Amber		= pin 16
# Row 2 Green		= pin 15

import urllib.request
from urllib.error import  URLError
from bs4 import BeautifulSoup as BS
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #Set the board mode. BCM Pinouts are different, hence BOARD
	
leds = [13, 12, 7, 18, 16, 15] #Set up the GPIO pins to be used

for n in leds: #Reset all LEDs
	GPIO.setup(n, GPIO.OUT)
	GPIO.output(n, False)

alert_url = "https://nagiosserver/alerts.html" 

def checkAlerts():
	try:

		with urllib.request.urlopen(alert_url, timeout = 3) as url:
			pageData = BS(url.read()) #Process with BeautifulSoup to work with the data
			red = len(pageData.findAll("tr", { "class" : "red" }))
			orange = len(pageData.findAll("tr", { "class" : "orange" }))
			green = len(pageData.findAll("tr", { "class" : "green" }))
			ippatrol = len(pageData.findAll("tr", { "class" : "ippatrol" }))
			print(red,orange,green,ippatrol)

	except URLError as e:
		if hasattr(e, 'reason'):
			print('We failed to reach a server.')
			print('Reason: ', e.reason)
			for n in leds:
				GPIO.output(n,GPIO.HIGH)
				sleep(1)
		elif hasattr(e, 'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code: ', e.code)
			for n in leds:
				GPIO.output(n,GPIO.HIGH)
				sleep(1)
	else:

		for n in leds:
			GPIO.output(n, False)
 
		if ippatrol > 0:  #If an IPPatrol alert comes up, that means a site is down, so flash all lights once
			for n in leds:
				GPIO.output(n,GPIO.HIGH)
				sleep(0.1)
				GPIO.output(n,GPIO.LOW)
				sleep(0.1)
				GPIO.output(n,GPIO.HIGH)
				sleep(0.1)
				GPIO.output(n,GPIO.LOW)
				GPIO.output(18,GPIO.HIGH) #Keep this one on after all lights have been flashed

		if red > 0:  #If something is wrong, light up the red light
			GPIO.output(13,GPIO.HIGH)

		if red > 5:  #If something is *really* wrong, flash the red light to grab my attention!
			GPIO.output(13,GPIO.LOW)
			sleep(0.2)
			GPIO.output(13,GPIO.HIGH)
			sleep(0.2)			
			GPIO.output(13,GPIO.LOW)
			sleep(0.2)
			GPIO.output(13,GPIO.HIGH)

		if orange > 0:
			GPIO.output(12,GPIO.HIGH)

		if green > 0:
			GPIO.output(7,GPIO.HIGH)

count = 0
while True:
	count += 1
	sleep (5)
	checkAlerts()

#except KeyboardInterrupt:
#	GPIO.cleanup()
