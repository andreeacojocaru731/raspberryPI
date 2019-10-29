# statie_meteo

Monitorizarea temperaturii ambientale

## Author : Cojocaru Andreea

Descriere:

Se salveaza temperatura la momentul pornirii aplicatiei ca si temperatura initiala.
Se verifica temperatura curenta cu valoarea initiala, iar in functie de diferenta dintre ele se va aprinde un led RGB intr-o anumita culoare.

Initial va fi verde, urmand sa varieze :
- in nuante de albastru, daca temperatura ambientala scade; 
- in nuante de la galben->portocaliu->rosu, daca temperatura e mai mare decat cea initiala.
Am ales ca si treapta, valoarea de 0.5 gradeC.

Proof of working: [video1](https://drive.google.com/open?id=0B717Bl1S-5MGR28zaVU1ak0xamc), [video2](https://drive.google.com/open?id=0B717Bl1S-5MGekNQS3dyakpsSTQ)
 
Componente fizice utilizate:

- placuta RaspberryPI B+
- card mSD 32GB
- senzor temperatura DS18B20 ( http://cdn.sparkfun.com/datasheets/Sensors/Temp/DS18B20.pdf )
- rezistor 4.7kohm
- led RGB APA-106-F8 ( https://cdn.sparkfun.com/datasheets/Components/LED/COM-12877.pdf )
- fire de legatura mama-tata
- fire de legatura tata-tata
- mini breadboard

Conexiuni:

- Se foloseste interfata GPIO a placutei Raspberry.
- La pinul 2 (VCC) al placutei Raspberry am legat alimentarea de 5V.
- Senzorul de temperatura se leaga astfel :
 - pinul 1 (GND) la pinul 6(GND) de la raspberry.
 - pinul 2 (DQ - date) la pinul 7 (GPIO4) de la raspberry.
 - pinul 3 (VCC) la pinul 2(VCC) de la raspberry.
- Rezistorul se cupleaza la pinii 2 si 3 ai senzorului de temperatura.
- Ledul are 4 pini, dupa cum urmeaza:
 - pinul 1 (DIN) - se leaga la pinul 12(GPIO18 - PWM) de la raspberry.
 - pinul 2 (VDD) - se leaga la pinul 2 de la raspberry.
 - pinul 3 (GND) - se leaga la pinul 3 de la raspberry.
 - pinul 4 (DOUT) - daca se folosesc leduri in serie, pinul 1 al ledului numarul 2 se leaga la pinul 4 al ledului numarul 1.

Detalii software:

- Pe RaspberryPI ruleaza SO Jessi.
- Pentru conectare am folosit programul Putty.
- Tipul legaturii este SSH pe portul 22.
- De obicei, este necesara logarea. 
- Userul predefinit este pi.
- Parola predefinita este raspberry.
- Pentru actualizarea OS se ruleaza :
sudo apt-get update
sudo apt-get upgrade
- Limbajul de programare ales este python.


Configurarea senzorului de temperatura :

- Se adauga linia 
dtoverlay=w1-gpio 
- in fisierul 
/boot/config.txt .
- Se iese din fisier si se ruleaza urmatoarele linii :
cd
sudo modprobe w1-gpio
sudo modprobe w1-therm

- Pentru accesarea fisierului in care vor fi salvate valorile citite se alege calea :
/sys/bus/w1/devices/
- Aici este creat automat un director ce difera ca nume de la un caz la altul 
( in situatia mea, denumirea este 28-0000075f800d ).
- In interiorul acestuia se regaseste fisierul ce ne intereseaza, si anume 
w1_slave.

Comandarea ledului :

- Am folosit https://github.com/jgarff/rpi_ws281x cu mentiunea ca am modificat fisierul ws2811.c, astfel :

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
