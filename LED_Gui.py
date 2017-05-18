import Tkinter
import pyfirmata
from time import sleep
def onStartButtonPress():
  startButton.config(state=Tkinter.DISABLED)
  ledPin.write(1)
  # LED is on for fix amount of time specified below
  sleep(5)
  ledPin.write(0)
  startButton.config(state=Tkinter.ACTIVE)
port = 'COM4'
board = pyfirmata.Arduino(port)
sleep(5)
ledPin = board.get_pin('d:11:o')
top = Tkinter.Tk()
top.title("Blink LED using button")
top.minsize(300,30)
startButton = Tkinter.Button(top,text="Start",command=onStartButtonPress)
startButton.pack()
top.mainloop()
