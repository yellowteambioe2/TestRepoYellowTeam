from gpiozero import LED
from time import sleep
from gpiozero import Button

led = LED(23)
button = Button(18)

button.wait_for_press()

print ('Cycle 1')
led.on()
sleep(1)
led.off()
sleep(1)

print ('Cycle 2')
led.on()
sleep(1)
led.off()
sleep(1)

print ('Cycle 3')
led.on()
sleep(1)
led.off()
sleep(1)

print ('Cycle 4') 
led.on()
sleep(1)
led.off()
sleep(1)

print ('Cycle 5')
led.on()
sleep(1)
led.off()
sleep(1)

print ('I cycled 5 times, turning the led on and then off for 1 second each')
