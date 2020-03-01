from datetime import datetime

if __name__=='__main__':
    fileName='InputTimes.txt'
    Date = []
    Doppler = []
    import csv
    # with open('/home/pi/GIT_GNU/GNU/GNU_code/Record_ref/Dummy.txt') as f:
    with open('./'+fileName) as f:
        reader=csv.reader(f,delimiter='\t')
        for row in reader:
            Str=str.split(row[0],"    ")
            print("Raw String: "+Str[0])
            h1=datetime.strptime(Str[0],"%Y-%m-%dT%H:%M:%S.%f")
            Date.append(h1)
            Doppler.append(float(Str[1]))
            print("Before Schedule utc: " + str(h1))