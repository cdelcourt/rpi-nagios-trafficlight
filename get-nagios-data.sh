#!/bin/sh

#get the html pages of the alert boards, ignore broken certs
wget -O /home/user/pi-nagios-lights/peer1/output --no-check-certificate https://url.goes.here/alerts.html
wget -O /home/user/pi-nagios-lights/ldn1/output --no-check-certificate https://url.goes.here/alerts.html

#grep necessary informations from the output for peer1 board
grep -e 'darkred\|red' /home/user/pi-nagios-lights/peer1/output | wc -l > /home/user/pi-nagios-lights/peer1/redalertcount
grep -e 'darkorange\|orange' /home/user/pi-nagios-lights/peer1/output | wc -l > /home/user/pi-nagios-lights/peer1/orangealertcount

#now for LDN board
grep -e 'darkred\|red' /home/user/pi-nagios-lights/ldn1/output | wc -l > /home/user/pi-nagios-lights/ldn1/redalertcount
grep -e 'darkorange\|orange' /home/user/pi-nagios-lights/ldn1/output | wc -l > /home/user/pi-nagios-lights/ldn1/orangealertcount
grep -e 'green' /home/user/pi-nagios-lights/ldn1/output | wc -l > /home/user/pi-nagios-lights/ldn1/greenalertcount
grep -e 'ippatrol' /home/user/pi-nagios-lights/ldn1/output | wc -l > /home/user/pi-nagios-lights/ldn1/ippatrolcount