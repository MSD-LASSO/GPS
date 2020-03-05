import L76X
import time
from datetime import datetime, date
import math
import os

os.system("sudo echo IRan! >> /home/pi/Documents/debugger.txt 2>&1")
# try:
x = L76X.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Set_Baudrate(115200)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)

x.L76X_Send_Command(x.SET_POS_FIX_100MS);

# Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);

# x.L76X_Exit_BackupMode();

# f = open("Coordinates.txt", "w+")

i = 1.000;
ALat = 0.000
ALon = 0.000
AAlt = 0.000


# Read the times from the input text file.
Date=[]
Doppler=[]

#IMPORTANT: Cannot have extra white space at end of InputTimes.txt. It will throw "index out of range" error
fileName='InputTimes.txt'
import csv
# with open('/home/pi/GIT_GNU/GNU/GNU_code/Record_ref/Dummy.txt') as f:
with open('/home/pi/GPS/Unification_Attempt/'+fileName) as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        Str=str.split(row[0],"    ")
        # print("Raw String: "+Str[0])
        h1=datetime.strptime(Str[0],"%Y-%m-%dT%H:%M:%S.%f")
        Date.append(h1)
        Doppler.append(float(Str[1]))
        print("Before Schedule utc: " + str(h1))
        os.system("sudo echo "+"Before Schedule utc: " + str(h1)+" >> /home/pi/Documents/debugger.txt 2>&1")

i=0
while (i<len(Date)):

    try:
        x.L76X_Get()
    except:
        os.system("sudo echo Failed To Get GPS >> /home/pi/Documents/debugger.txt 2>&1")
        x.Status="0"
    # print('\n')

    #Get the current time to the best of our ability.
    if (x.Status == "1"):
        GPS=True;
        # 2020-3-1
        # 20:17:2.5
        Str=x.Date+'T'+x.Time
        # Str='2020-3-1'+'T'+'20:17:2.5'
        currentTime = datetime.strptime(Str, "%Y-%m-%dT%H:%M:%S.%f")

        # currentTime=datetime.now()

        # print('Position aquired')

        # print("Date: " + x.Date)
        # print("Time: " + x.Time)
        # print('Lat = %f' % x.Lat)
        # print('Lon = %f' % x.Lon)
        # print('Alt = %f' % x.Alt)

        # ALat = (ALat * (1 - (1 / i))) + (x.Lat * (1 / i))
        # ALon = (ALon * (1 - (1 / i))) + (x.Lon * (1 / i))
        # AAlt = (AAlt * (1 - (1 / i))) + (x.Alt * (1 / i))

        # print('ALat = %f' % ALat)
        # print('ALon = %f' % ALon)
        # print('AAlt = %f' % AAlt)

        # os.system('sudo timedatectl set-time \'' + x.Date + ' ' + x.Time + '\'')
        # f.write(
        #     '%f' % x.Lat + ' %f' % x.Lon + ' %f' % x.Alt + ' %0.f:' % x.Time_H + '%0.f:' % x.Time_M + '%.2f' % x.Time_S + '\n')

        # i = i + 1

    else:
        # print('No positioning')
        GPS=False
        currentTime=datetime.now()

    # Compare current time and the set times.
    print(currentTime)
    os.system("sudo echo Using GPS "+ str(GPS)+' Time '+ str(currentTime) + " >> /home/pi/Documents/debugger.txt 2>&1")
    if currentTime>=Date[i]:
        # print('Scheduled Time: '+str(Date[i]))

        # String = datetime.now()
        # print('Before Function Call: '+str(String))

        ######################### Start Function Call #########################
        # String='python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq='+str(int(round(Doppler*1e6)))+' --samp-rate=2000000 --center-freq=437000000 --num-samples=10000000 --file-loc="/home/pi/Documents/Time'+str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+'"'
        # String='python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq='+'162400000'+' --samp-rate=2000000 --center-freq=162000000 --num-samples=10000000 --file-loc="/home/pi/Documents/Time'+str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+'"'
        # String='python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq='+'97900000'+' --samp-rate=2000000 --center-freq=97000000 --num-samples=10000000 --file-loc="/home/pi/Documents/Time'+str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+'"'
        if Doppler[i] > 0:
            String='python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq='+str(int(round(Doppler[i]*1e6)))+' --samp-rate=2000000 --center-freq=437000000 --num-samples=1800000000 --file-loc="/home/pi/Documents/Time'+str(currentTime).replace(" ","_").replace(":","_").replace(".","_")+'"'
            # String = 'python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq=' + '437200000' + ' --samp-rate=2000000 --center-freq=437000000 --num-samples=12000000 --file-loc="/home/pi/Documents/Time' + str(
            #     currentTime).replace(" ", "_").replace(":", "_").replace(".", "_") + '"'
        else:
            # String='python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq='+'162400000'+' --samp-rate=2000000 --center-freq=162000000 --num-samples=10000000 --file-loc="/home/pi/Documents/Time'+str(datetime.now()).replace(" ","_").replace(":","_").replace(".","_")+'"'
            String = 'python /home/pi/GIT_GNU/GNU/GNU_code/Record_ref/record_ref.py --channel-freq=' + '97900000' + ' --samp-rate=2000000 --center-freq=97000000 --num-samples=10000000 --file-loc="/home/pi/Documents/Time' + str(
                currentTime).replace(" ", "_").replace(":", "_").replace(".", "_") + '"'

        # time.sleep(10)
        # String="date >> /home/pi/Documents/debugger.txt 2>&1"
        # String="date >> /home/pi/Documents/TimingTest.txt 2>&1"
        print(Doppler)
        print(String)
        os.system("sudo echo "+String+" >> /home/pi/Documents/debugger.txt 2>&1")
        os.system(String)
        ######################### End Function Call #########################


        # String = datetime.now()
        # print('After Function Call: '+str(String))

        # print('\n')
        i+=1

        if i>=len(Date):
            # print("All scheduled Times Completed")
            break
    else:
        # Time has not lined up yet, continue.
        continue

os.system("sudo echo All Scheduled Times Completed >> /home/pi/Documents/debugger.txt 2>&1")
print("All scheduled Times Completed")






