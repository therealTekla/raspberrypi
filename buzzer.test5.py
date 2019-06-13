from gpiozero import Button, LED
from time import sleep
from gpiozero import Buzzer

#BuzzPin = 32 # Raspberry Pi Pin 12-GPIO 12

wartezeit = 5
gruen_fuer_fussgaenger = 10

button = Button(21)

red1 = LED(27)
green1 = LED(4)

red2 = LED(26)
yellow2 = LED(13)
green2 = LED(5)


bz = Buzzer(12)

def beep():
    bz.beep(0.5, 0.5, None, True)


def loop():
    while True:
        beep(1)


#if __name__ == "__main__":
 #   setup(BuzzPin)
  #  try:
   #     loop()
    #except KeyboardInterrupt:
     #   destroy()


def change():

    sleep(wartezeit)
    green2.off()
    yellow2.on()
    sleep(1.5)
    yellow2.off()
    red2.on()
    sleep(1.5)
    
    red1.off()
    green1.on()
    beep()
    sleep(gruen_fuer_fussgaenger)
    green1.off()
    bz.off()
    red1.on()
    sleep(1.5)

    yellow2.on()
    sleep(1.5)
    red2.off()
    yellow2.off()
    green2.on()

red1.on()
green2.on()
button.when_pressed = change
