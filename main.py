import L76X
import time
import math
import os

#Set python baudrate to 9600 to initially communicate with chip
x=L76X.L76X()
x.L76X_Set_Baudrate(9600)

#Set chip baudrate to 115200 to get maximum data rate
#For some reason it sometimes doesnt set on the first coammand to the command it sent three times to ensure chip recieves it
#This issue only happens on cold boot of raspberry pi
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)

#Set python baudrate to 115200 to communicate with chip
x.L76X_Set_Baudrate(115200)

#Set chip baudrate to 115200 one more time for good measure
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)

#Set update rate
x.L76X_Send_Command(x.SET_POS_FIX_100MS);

#Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

#Write outputs to a file "Coordinates.txt"
f=open("Coordinates.txt", "w+")

#Variables used to take rolling average of Lat, Lon, and Alt
i = 1.000;
ALat = 0.000
ALon = 0.000
AAlt = 0.000

#While loop that has program run until force stopped
while(1 == 1):
    x.L76X_Get()
    print '\n'
    if(x.Status == "1"):
        print 'Position aquired'
        
        #Print date and time in UTC
        print "Date: " + x.Date
        print "Time: " + x.Time
        
        #Print latitude, longitude, and altitude
        print 'Lat = %f'%x.Lat,
        print 'Lon = %f'%x.Lon,       
        print 'Alt = %f'%x.Alt
        
        #Calculate rollig average of lat, lon, and alt
        ALat = (ALat * (1 - (1/i))) + (x.Lat * (1/i))
        ALon = (ALon * (1 - (1/i))) + (x.Lon * (1/i))
        AAlt = (AAlt * (1 - (1/i))) + (x.Alt * (1/i))
        
        #Print rolling averages
        print 'ALat = %f'%ALat,
        print 'ALon = %f'%ALon,       
        print 'AAlt = %f'%AAlt
        
        #Experimental way of setting Raspberry Pi system time to GPS Time. Doing it this way is not reccommended due to overhead reasons
        #os.system('sudo timedatectl set-time \'' + x.Date + ' ' + x.Time+'\'')
        
        #Log the lat, lon, alt, and time
        f.write('%f'%x.Lat + ' %f'%x.Lon + ' %f'%x.Alt + ' %0.f:'%x.Time + '\n')
        
        i = i+1 

    else:
        print 'No positioning'

