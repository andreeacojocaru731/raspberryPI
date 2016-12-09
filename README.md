# statie_meteo

Citire temperatura de la un senzor digital. 

## Author : Cojocaru Andreea

Am folosit https://github.com/jgarff/rpi_ws281x cu mentiunea ca am modificat fisierul ws2811.c, astfel :

```diff

--- a/ws2811.c
+++ b/ws2811.c
@@ -55,16 +55,16 @@

 /* 4 colors (R, G, B + W), 8 bits per byte, 3 symbols per bit + 55uS low for reset signal */
 #define LED_COLOURS                              4
-#define LED_RESET_uS                             55
-#define LED_BIT_COUNT(leds, freq)                ((leds * LED_COLOURS * 8 * 3) + ((LED_RESET_uS * \
-                                                  (freq * 3)) / 1000000))
+#define LED_RESET_uS                             50
+#define LED_BIT_COUNT(leds, freq)                ((leds * LED_COLOURS * 8 * 5) + ((LED_RESET_uS * \
+                                                  (freq * 5)) / 1000000))

 // Pad out to the nearest uint32 + 32-bits for idle low/high times the number of channels
-#define PWM_BYTE_COUNT(leds, freq)               (((((LED_BIT_COUNT(leds, freq) >> 3) & ~0x7) + 4) + 4) * \
+#define PWM_BYTE_COUNT(leds, freq)               (((((LED_BIT_COUNT(leds, freq) >> 5) & ~0x7) + 4) + 4) * \
                                                   RPI_PWM_CHANNELS)

-#define SYMBOL_HIGH                              0x6  // 1 1 0
-#define SYMBOL_LOW                               0x4  // 1 0 0
+#define SYMBOL_HIGH                               11110
+#define SYMBOL_LOW                                10000


 // We use the mailbox interface to request memory from the VideoCore.
@@ -672,7 +672,7 @@ ws2811_return_t ws2811_render(ws2811_t *ws2811)
                         symbol = SYMBOL_HIGH;
                     }

-                    for (l = 2; l >= 0; l--)               // Symbol
+                    for (l = 4; l >= 0; l--)               // Symbol
                     {
                         uint32_t *wordptr = &((uint32_t *)pwm_raw)[wordpos];
```
