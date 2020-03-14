import serial  # pip install serial   or pip install pyserial in    cmd or terminal or pycharm virtual terminal
import time

# ser is a filehandler
ser = serial.Serial('COM6',9600)   #specify your port

time.sleep(2)
time.sleep(2)

a = ser.readline()  #Read line from Serial Monitor
a = a.decode()
a = a.rstrip()
print(a)   #It will print HI
