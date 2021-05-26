import RPi.GPIO as GPIO
import time

sensorInf = 37
sensorSup = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorInf,GPIO.IN)
GPIO.setup(sensorSup,GPIO.IN)

print "IR Sensor Ready....."
print " "

try: 
	while True:
		#sensor = not sensor
		if GPIO.input(sensorInf) and GPIO.input(sensorSup): #No hay nada en el sensor
			print "NO Object Detected"
			#mover motor
		elif GPIO.input(sensorInf):
			print "NO Object DetectedS inf"
			#mover motor
		elif GPIO.input(sensorSup):
			print "NO Object DetectedS Sup" 
			#mover motor	
		else:#objeto detectado
			print "Object Detected"
			#detener motor
			#encender bomba
			
			
except KeyboardInterrupt:
	GPIO.cleanup()

