import time
import datetime
import urllib

from neopixel import *

LED_COUNT = 1
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 100
LED_INVERT = False
LED_STRIP = ws.SK6812_STRIP
LED_CHANNEL = 0

COLOR_LIST = [Color(255,0,0),Color(255,0,0),Color(0,255,0)]

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

device_file = "/sys/bus/w1/devices/28-0000075f800d/w1_slave"


def readTemperature():
        file = open(device_file, "r")
        data = file.read()
        file.close()

        (discard,sep,reading) = data.partition('t=')
        temperature = float(reading)/1000.0

        print(str(datetime.datetime.now())+" : "+sep+" "+str(temperature)+" gradeC")

        return temperature

while True:
        #strip.setPixelColor(0,Color(255,0,0)) #Green
        #strip.setPixelColor(0,Color(0,255,0)) #Red
        #strip.setPixelColor(0,Color(0,0,255)) #Blue


        temperature = readTemperature()

        if (temperature > 23.0) is True :
                strip.setPixelColor(0,COLOR_LIST[2])
                strip.show()
                time.sleep(0.1)
        else:
                strip.setPixelColor(0,COLOR_LIST[1])
                strip.show()
                time.sleep(0.1)
