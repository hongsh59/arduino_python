# Import required libraries
# User must install pyfirmata in shell
# pip -m install pyfirmata 
import pyfirmata
from time import sleep

# Define custom function to perform Blink action
def blinkLED(pin, message):
    print message
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)
# Associate port and board with pyFirmata
port ='COM4'
board = pyfirmata.Arduino(port)

# Use iterator thread to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Define pins
pirPin = board.get_pin('d:7:i')
redPin = 12
greenPin = 13

# Check for PIR sensor input
while True:
   # Ignore case when receiving None value from pin
   value = pirPin.read()
   print(value)
#  while value is None:
#      pass
   if value is None:
      print("Disconnected")
      sleep(1)
   elif value is True:
      # Perform Blink using custom function
      blinkLED(redPin, "Motion Detected")
   elif value is False:
      # Perform Blink using custom function
      blinkLED(greenPin, "No motion Detected")
# Release the board
board.exit()
