Preface: Please note that this is the first time I've done programming in well.. ever. That's my excuse.

This is an experiment I thought up a while ago to hook up some LEDs to my Raspberry Pi and use them to monitor the status of the alert board at work and have it shine or flash one of the LEDs via the RPi GPIO output when an alert comes up.

Initially, I set up a bash script that fed via STDIN to a Python script, but I knew this was inherently a BadIdea(tm) but it allowed me to get a functional version, which was 0.1. After some useful guideance from my explodingly awesome mentor, idris, I did some research and trial-and-erroring to rewrite it sans the bash script and had it working independently of any other files or inputs, using urllib and BeautifulSoup to grab the HTML and sort through it.

The code looks up our nagios alert board which is an HTML page and the script scrapes the tables for the right tags and counts them. The TR tags that it searches for in the script are the rows that individual alerts show up on and the TR tags have the colours in them for what kind of alerts they are (red, orange, green, or ippatrol, which is if one of our websites is down).

![](http://img.photobucket.com/albums/v234/Anode/IMG_20140107_113546_zps76630bd8.jpg)

It's got some basic error handling for if the monitoring board URL itself wasn't available but other than that, it's a bit dumb.

Ultimately, this would be cool to do if I wanted to hook up some relays to the GPIOs and have big lights to really highlight errors going on, but this was really a see-if-i-could-do-it kind of project. Now it's done, I'm keen to find out what else I can code and additionally, how I can improve upon this and make it better. Thus far, I'm thinking of email alerts or some kind of alert to my phone when I'm away from my desk.

Suggestions, comments and criticisms welcome :)

~cdelcourt

=========================================================

For reference, I will be testing this on the following GPIO add-on board to test this all out:

http://www.rapidonline.com/Electronic-Components/Pi-O-Raspberry-Pi-Input-Output-Board-73-5230
