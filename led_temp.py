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

COLOR_LIST = [Color(0,0,255),Color(179,0,230),Color(255,0,0),Color(255,255,0),Color(204,255,0),Color(102,255,0),Color(0,255,0)]

#Color(  G,  R,  B)
		
#Color(  0,  0,255), 0 - blue
#Color(179,  0,230), 1 - light blue
#Color(255,  0,  0), 2 - green
#Color(255,255,  0), 3 - yellow
#Color(204,255,  0), 4 - ocru
#Color(102,255,  0), 5 - orange
#Color(  0,255,  0), 6 - red

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

print ('Ctrl-C to quit !')

device_file = "/sys/bus/w1/devices/28-0000075f800d/w1_slave"


def readTemperature():

        file = open(device_file, "r")
        data = file.read()
        file.close()

        (discard,sep,reading) = data.partition('t=')
        temperature = float(reading)/1000.0

        print(str(datetime.datetime.now())+" : "+sep+" "+str(temperature)+" gradeC")

        return temperature

def changeColor(index):
        strip.setPixelColor(0,COLOR_LIST[index])
        strip.show()
        time.sleep(0.1)

        return

initialTemp = readTemperature()

while True:

        temperature = readTemperature()


	if ((temperature >= (initialTemp - 0.5) ) and (temperature <= (initialTemp + 0.5) ))  is True :
                changeColor(2)
        elif (temperature < (initialTemp - 1)) is True :
                changeColor(0)
        elif (temperature < (initialTemp - 0.5)) is True :
                changeColor(1)
        elif (temperature > (initialTemp + 2)) is True :
                changeColor(6)
        elif (temperature > (initialTemp + 1.5)) is True :
                changeColor(5)
        elif (temperature > (initialTemp + 1)) is True :
                changeColor(4)
        elif (temperature > (initialTemp + 0.5)) is True :
                changeColor(3)

