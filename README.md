Preface: Please note that this is the first time I've done programming in well.. ever really. That's my excuse. What's yours?

This is an experiment I thought up a while ago to hook up some LEDs to my Raspberry Pi and use them to monitor the status of the alert board at work and have it shine or flash one of the LEDs via the RPi GPIO output when an alert comes up.

At the moment, the idea is that

1) Batch script runs, dumps it all to the 'output' file where the information is then grep'd, looking for various HTML colours to indicate what kind of alerts are on the board. The 
2) Python script reads the files and generally, if the values are above 0 for a given error type, it will turn on one of the LEDs via the GPIO module
3) I panic because the LED flashes, because something is broken

This is an unbelievably convuluted way of going about it I know, but with my limited knowledge of python I wasn't sure how best to go about this. The way of doing this would probably have to be heavily modified for it to work with anything else, but if anything, hopefully maybe parts of it could be useful for someone.

As of right now (30/10/2013) this is currently all untested and probably doesn't work. Hoping to test this out in the next few weeks and will obviously update on progress as I make any.

=========================================================

For reference, I will be testing this on the following GPIO add-on board to test this all out:

http://www.rapidonline.com/Electronic-Components/Pi-O-Raspberry-Pi-Input-Output-Board-73-5230

