# Graphical User Interface for the Bluetooth sensor
# Imports
import time
import serial
try :
	from Tkinter import*  # for 2.7
except ImportError:
	from tkinter import*   # for 3.3
# Serial port parameters
serial_speed =9600
serial_port ='COM4'
# Test with USB-Serial connection
# serial_port = '/dev/tty.usbmodem1421'
ser = serial.Serial(serial_port, serial_speed, timeout=1)
# Main Tkinter application
class Application(Frame):
	# Measure data from the sensor
	def measure(self):
		# Request data and read the answer
		ser.write(b"m")
		data = ser.readline()
		print(data)
		# If the answer is not empty, process & display data
		if (data !="b\'\'"):
			processed_data = data.split(b",")
			temp =str(processed_data[0][0:5])
			humi =str(processed_data[1][0:5])
			self.temp_data.set("Temperature: "+ temp[2:7])
			self.temperature.pack()
			self.hum_data.set("Humidity: "+ humi[2:7])
			self.humidity.pack()
		# Wait 1 second between each measurement
		self.after(1000,self.measure)
	# Create display elements
	def createWidgets(self):
		self.temperature = Label(self, textvariable=self.temp_data, font=('Verdana', 40, 'bold'))
		self.temp_data.set("Temperature")
		self.temperature.pack()
		self.humidity = Label(self, textvariable=self.hum_data, font=('Verdana', 40, 'bold'))
		self.hum_data.set("Humidity")
		self.humidity.pack()
	# Init the variables & start measurements
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.temp_data = StringVar()
		self.hum_data = StringVar()
		self.createWidgets()
		self.pack()
		self.measure()
# Create and run the GUI
root = Tk()
app = Application(master=root)
app.mainloop()