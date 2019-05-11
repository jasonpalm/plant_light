#!/usr/bin/python3

import RPi.GPIO as gpio
import datetime as dt
import sys

start = 4    # 4 AM
end = 22     # 10 PM
pin = 4
hour = dt.datetime.now().hour

def usage():
    print("\nUsage: {} auto|on|off\n".format(sys.argv[0]))

def on():
    print('on')
    gpio.output(pin, gpio.HIGH)

def off():
    print('off')
    gpio.output(pin, gpio.LOW)

def auto():
    if (start <= hour <= end):
        on()
    else:
        off()
    end

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

if (len(sys.argv) != 2):
    usage()
    exit(1)
end

arg = sys.argv[1].lower()
if (arg == 'auto'):
    auto()
elif (arg == 'on'):
    on()
elif (arg == 'off'):
    off()
end

