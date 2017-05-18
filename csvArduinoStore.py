# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

import csv
import pyfirmata
from time import sleep

filename = "csvReadFromArduino.csv"
port = 'COM4'
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

pirPin = board.get_pin('d:11:i')
a0 = board.get_pin('a:0:i')
try :
  f = open(filename, 'w+', newline='')
except :
  f = open(filename, 'w+')

w = csv.writer(f)
w.writerow(["Number", "Potentiometer", "Motion sensor"])
i = 0
while i < 25:
  sleep(1)
  print("work")
  pirData = pirPin.read()
  potData = a0.read()
  if pirData is not None :
    i += 1
    row = [i, potData, pirData]
    w.writerow(row)

print("Done. CSV file is ready!")
board.exit()
