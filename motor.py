import serial  
import time  
print ("Start")  
port="COM5"  
bluetooth=serial.Serial(port,9600,5)  
print("Connected")  
bluetooth.flushInput()  
for i in range(5): 
  print("ping")  
  bluetooth.write(b"Boop "+str.encode(str(i)))  
  input_data = bluetooth.readline()  
  print(input_data.decode())  
  time.sleep(0.1)  
bluetooth.close()  
print("Done")