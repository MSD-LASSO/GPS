import L76X
import time
import math

# try:
x=L76X.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(5)
x.L76X_Set_Baudrate(115200)

x.L76X_Send_Command(x.SET_POS_FIX_100MS);

#Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

x.L76X_Exit_BackupMode();

f=open("Coordinates.txt", "w+")

i = 1.000;
ALat = 0.000
ALon = 0.000
AAlt = 0.000

while(1 == 1):
    x.L76X_Get()
    print '\n'
    if(x.Status == "1"):
        print 'Position aquired'
    
        print 'Time %d:'%x.Time_H,
        print '%d:'%x.Time_M,
        print '%.2f'%x.Time_S
    
        print 'Lat = %f'%x.Lat,
        print 'Lon = %f'%x.Lon,       
        print 'Alt = %f'%x.Alt
    
        ALat = (ALat * (1 - (1/i))) + (x.Lat * (1/i))
        ALon = (ALon * (1 - (1/i))) + (x.Lon * (1/i))
        AAlt = (AAlt * (1 - (1/i))) + (x.Alt * (1/i))
    
        print 'ALat = %f'%ALat,
        print 'ALon = %f'%ALon,       
        print 'AAlt = %f'%AAlt

        f.write('%f'%x.Lat + ' %f'%x.Lon + ' %0.f:'%x.Time_H + '%0.f:'%x.Time_M + '%.2f'%x.Time_S + '\n')
        
        i = i+1 

    else:
        print 'No positioning'

