from gpiozero import Button, LED
from time import sleep



button = Button(17)
blue = LED(22)


green = LED(15)
yellow = LED(23)
red = LED(25)




while True:
    if button.is_pressed:
        blue.on()
        sleep(3)
    else:
        blue.off()
        sleep(0.25)
    blue.off()
    sleep(1)
    green.on()
    sleep(3)
    green.off()
    yellow.on()
    sleep(1.5)
    yellow.off()
    red.on()
    sleep(2.5)
    yellow.on()
    sleep(1)
    red.off()
    yellow.off()
    
