#la bomba esta conectada en el GPIO 23 -> pin 16
#la bomba prende con un 0 logico
#sensor inferior GPIO 26 -> pin 37
#sensor superior GPIO 19 -> pin 35

import time
import RPi.GPIO as GPIO


pinBomba = 16
sleepBomba = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinBomba,GPIO.OUT)

def bombaOn():
	GPIO.output(pinBomba,GPIO.LOW)
	print "Bomba encendida"
	time.sleep(sleepBomba)
	
	
def bombaOff():
	GPIO.output(pinBomba,GPIO.HIGH)
	print "Bomba apagada"
	time.sleep(sleepBomba)
	
def bomba():
	while(1):
		bombaOn()
		bombaOff()
	
try:
    bomba()
              
except KeyboardInterrupt:
    GPIO.cleanup()
    
finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO
