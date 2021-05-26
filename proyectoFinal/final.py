import RPi.GPIO as GPIO
import time
import drivers
from time import sleep

GPIO.setmode(GPIO.BOARD)

#para la bomba

pinBomba = 16
sleepBomba = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinBomba,GPIO.OUT)

def bombaOn():
	GPIO.output(pinBomba,GPIO.LOW) #la bomba prende con un 0 logico
	print "Bomba encendida"
	time.sleep(sleepBomba)
	bombaOff()
	
	
def bombaOff():
	GPIO.output(pinBomba,GPIO.HIGH) #la bomba apaga con un 1 logico
	print "Bomba apagada"
	#time.sleep(sleepBomba)

#para los sensores
sensorInf = 37
sensorSup = 35
GPIO.setup(sensorInf,GPIO.IN)
GPIO.setup(sensorSup,GPIO.IN)

#para el LCD
display = drivers.Lcd()

def llenando():
        display.lcd_clear() 
        display.lcd_display_string("Llenando envase", 1)  
        display.lcd_display_string("Por favor espera", 2)  

def lleno():
        display.lcd_clear() 
        display.lcd_display_string("Envase lleno", 1)  
        display.lcd_display_string("Cambiando envase", 2) 
   
#para el nema17

out1 = 13
out2 = 11
out3 = 15
out4 = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)


def nema():
	i=0
	positive=0
	negative=0
	y=0
	timeSleep =.003		#.03
	
	GPIO.output(out1,GPIO.LOW)
	GPIO.output(out2,GPIO.LOW)
	GPIO.output(out3,GPIO.LOW)
	GPIO.output(out4,GPIO.LOW)
	x = 400
	if x>0 and x<=400:
		for y in range(x,0,-1):
			if negative==1:
				if i==7:
					i=0
				else:
					i=i+1
				y=y+2
				negative=0
			positive=1
			#print((x+1)-y)
			if i==0:
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==1:
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==2:  
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==3:    
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==4:  
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==5:
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==6:    
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==7:    
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			if i==7:
				i=0
				continue
			i=i+1
	elif x<0 and x>=-400:
		x=x*-1
		for y in range(x,0,-1):
			if positive==1:
				if i==0:
					i=7
				else:
					i=i-1
				y=y+3
				positive=0
			negative=1
			#print((x+1)-y) 
			if i==0:
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==1:
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==2:  
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==3:    
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.HIGH)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==4:  
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.LOW)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==5:
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.HIGH)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==6:    
				GPIO.output(out1,GPIO.LOW)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			elif i==7:    
				GPIO.output(out1,GPIO.HIGH)
				GPIO.output(out2,GPIO.LOW)
				GPIO.output(out3,GPIO.LOW)
				GPIO.output(out4,GPIO.HIGH)
				time.sleep(timeSleep)
				#time.sleep(1)
			if i==0:
				i=7
				continue
			i=i-1      

print "Despachador Listo....."
print " "

try: 
	while True:
		display.lcd_clear()
		if GPIO.input(sensorInf) and GPIO.input(sensorSup): #No hay nada en el sensor
			print "NO Object Detected"
			lleno()
			bombaOff()
			nema()
			time.sleep(sleepBomba)
			#mover motor
		elif GPIO.input(sensorInf):
			print "NO Object DetectedS inf"
			lleno()
			bombaOff()
			nema()
			#mover motor
		elif GPIO.input(sensorSup):
			print "NO Object DetectedS Sup" 
			lleno()
			bombaOff()
			nema()
			#mover motor	
		else:#objeto detectado
			print "Object Detected"
			llenando()
			bombaOn()
			#detener motor
			#encender bomba
			
			
except KeyboardInterrupt:
	GPIO.cleanup()

