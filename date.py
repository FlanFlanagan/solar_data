import datetime
import pytz
import numpy as np

from pysolar.solar import *

lat = 40.0149856
lon = -105.2705456

timezone = pytz.timezone('America/Denver')

times = []
degs = []
rads = []

months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def printfunc():
    date = datetime.datetime(2010, 6, 1, 15, 00, 00, tzinfo=timezone)
    deg = get_altitude(lat, lon, date)
    print(deg, np.sin(deg))

def loop():
    for k,v in months.items():
        m = k
        for d in range(v):
            day = d+1
            for h in range(24):
                for mi in range(2):
                    date = datetime.datetime(2010, m, day, h, mi*30, 0, tzinfo=timezone)
                    times.append(date)
                    deg = get_altitude(lat, lon, date)
                    if deg < 0:
                        deg = 0
                    degs.append(deg)
                    rads.append(1300.*np.sin(np.pi*deg/180.))

    with open('data.txt', 'w') as f:
        for i in range(len(times)):
            out = str(times[i]) + " " + str(degs[i]) + " " + str(rads[i])
            f.write(out)
    import matplotlib.pyplot as plt
    plt.figure(1)
    plt.subplot(211)
    plt.plot(rads)
    plt.subplot(212)
    plt.plot(degs)
    plt.savefig('degsR.png')

loop()
