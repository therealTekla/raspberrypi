from gpiozero import Button
from time import sleep



button = Button(22)


while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(5)




    

from gpiozero import LED
from time import sleep

green = LED(15)
yellow = LED(23)
red = LED(25)




while True:
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



