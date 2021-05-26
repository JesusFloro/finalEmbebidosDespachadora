

# imnportar las librerias
import drivers
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

def llenando():
        display.lcd_clear() 
        display.lcd_display_string("Llenando envase", 1)  
        display.lcd_display_string("Por favor espera", 2)  

def lleno():
        display.lcd_clear() 
        display.lcd_display_string("Envase lleno", 1)  
        display.lcd_display_string("Cambiando envase", 2) 
        
# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        llenando()
        sleep(2)                                           # Give time for the message to be read
        lleno()   # Refresh the first line of display with a different message
        sleep(2)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(2)                                           # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
