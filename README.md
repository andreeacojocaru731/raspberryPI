# statie_meteo

Citire temperatura de la un senzor digital. 

## Author : Cojocaru Andreea

Am folosit https://github.com/jgarff/rpi_ws281x cu mentiunea ca am modificat fisierul ws2811.c, astfel :

 #define LED_RESET_uS                             50
 #define LED_BIT_COUNT(leds, freq)                ((leds * LED_COLOURS * 8 * 5) + ((LED_RESET_uS * \ (freq * 5)) / 1000000))
                                                  
 #define PWM_BYTE_COUNT(leds, freq)               (((((LED_BIT_COUNT(leds, freq) >> 5) & ~0x7) + 4) + 4) * \ RPI_PWM_CHANNELS)

 #define SYMBOL_HIGH                               11110
 #define SYMBOL_LOW                                10000

##############################################################################################################################

 for (l = 4; l >= 0; l--)
   {
          uint32_t *wordptr = &((uint32_t *)pwm_raw)[wordpos];

          *wordptr &= ~(1 << bitpos);
          if (symbol & (1 << l))
          {
              *wordptr |= (1 << bitpos);
          }

          bitpos--;
          if (bitpos < 0)
          {
              // Every other word is on the same channel
              wordpos += 2;

              bitpos = 31;
          }
      }
