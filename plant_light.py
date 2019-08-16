#!/usr/bin/python3

# A simple script for the raspberry pi 2+ to turn a plant light on and off on schedule
# (See pinout below) 
start = 6    # 
end   = 18   # 
pin   = 4    # GPIO4

# J8:
#    3V3  (1) (2)  5V
#  GPIO2  (3) (4)  5V
#  GPIO3  (5) (6)  GND
#  GPIO4  (7) (8)  GPIO14
#    GND  (9) (10) GPIO15
# GPIO17 (11) (12) GPIO18
# GPIO27 (13) (14) GND
# GPIO22 (15) (16) GPIO23
#    3V3 (17) (18) GPIO24
# GPIO10 (19) (20) GND
#  GPIO9 (21) (22) GPIO25
# GPIO11 (23) (24) GPIO8
#    GND (25) (26) GPIO7
#  GPIO0 (27) (28) GPIO1
#  GPIO5 (29) (30) GND
#  GPIO6 (31) (32) GPIO12
# GPIO13 (33) (34) GND
# GPIO19 (35) (36) GPIO16
# GPIO26 (37) (38) GPIO20
#    GND (39) (40) GPIO21

import RPi.GPIO as gpio
import datetime as dt
import sys

def usage():
    print("\nUsage: {} auto|on|off\n".format(sys.argv[0]))

def on():
    gpio.output(pin, gpio.HIGH)

def off():
    gpio.output(pin, gpio.LOW)

def auto():
    hour = dt.datetime.now().hour
    turn_on = start <= hour < end
    if start > end:
        turn_on = not turn_on
    if turn_on:
        on()
    else:
        off()
    end

if (len(sys.argv) != 2):
    usage()
    exit(1)
end

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

arg = sys.argv[1].lower()
if (arg == 'auto'):
    auto()
elif (arg == 'on'):
    on()
elif (arg == 'off'):
    off()
end

