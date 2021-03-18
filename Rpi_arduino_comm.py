import RPi.GPIO as gpio
import time
import serial
import math
global ser
global ser2
import pathlib


ser = serial.Serial(
  
   port='/dev/ttyS0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)


   
    

while True:

    try:
        line=ser.readline()
        line1=line.rstrip().decode()
        print(line1)
        
                
        path = "//home/pi/modem-data-files/data.csv" 
        p = pathlib.Path(path)
        
        with open(path, "a+") as file:
            file.write(str(line1))
            
                
    except Exception as e:
        print("error occured: ",e)

        