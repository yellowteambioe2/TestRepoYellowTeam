from gpiozero import LED
from time import sleep
from gpiozero import Button

led = LED(23)
button = Button(18)

button.wait_for_press()

i = 1

while True :

    if i <= 5:

        led.on()
        sleep(1)
        led.off()
        sleep(1)

        print ('Cycle:  ', i)

        i = i+1

    else:
        i = 1
        button.wait_for_press()
