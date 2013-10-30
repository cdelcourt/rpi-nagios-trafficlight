#!/bin/sh

#get the html pages of the alert boards, ignore broken certs
wget -O /home/user/pi-nagios-lights/site2/output --no-check-certificate https://url.goes.here/alerts.html
wget -O /home/user/pi-nagios-lights/site1/output --no-check-certificate https://url.goes.here/alerts.html

#grep necessary informations from the output for site2 board
grep -e 'darkred\|red' /home/user/pi-nagios-lights/site1/output | wc -l > /home/user/pi-nagios-lights/site1/redalertcount
grep -e 'darkorange\|orange' /home/user/pi-nagios-lights/site1/output | wc -l > /home/user/pi-nagios-lights/site1/orangealertcount
grep -e 'green' /home/user/pi-nagios-lights/site1/output | wc -l > /home/user/pi-nagios-lights/site1/greenalertcount
grep -e 'ippatrol' /home/user/pi-nagios-lights/site1/output | wc -l > /home/user/pi-nagios-lights/site1/ippatrolcount

#now for site1 board
grep -e 'darkred\|red' /home/user/pi-nagios-lights/site2/output | wc -l > /home/user/pi-nagios-lights/site2/redalertcount
grep -e 'darkorange\|orange' /home/user/pi-nagios-lights/site2/output | wc -l > /home/user/pi-nagios-lights/site2/orangealertcount
