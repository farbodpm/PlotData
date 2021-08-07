import csv
import json
import re
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.widgets import Button
import pandas as pd
path = "C:\\Users\\Mahdyyar\\Desktop\\2581_data.csv"
path = "C:\\Users\\Mahdyyar\\Desktop\\2581_10.csv"

with open(path) as csvfile:
	data = {}
	data['lat'] = []
	data['lng'] = []
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
	for row in spamreader:
                x = re.findall("\((.*?)\)", row[2])
                for a in x:
                    y = re.findall("\'(.*?)\'", a)
                    if y[0] == "lng":
                        data['lng'].append(float(a.split(",")[1]))
                    elif y[0] == "lat":
                        data['lat'].append(float(a.split(",")[1]))
	df = pd.DataFrame(data=data)	
	df.to_csv("lat_lng_data.csv")         


datatype = "ignition"#"ignition"signalstrength
time = []
data = []
timesignalstrength = []
signalstrength = []
fig, ax = plt.subplots()

ax.set_autoscale_on(True)
ax.autoscale_view(True,True,True)
plt.subplots_adjust(bottom=0.2)
with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')

        for row in spamreader:
                 x = re.findall("\((.*?)\)", row[2])
                 if ("-07") in row[1]:
                     for a in x:
                        y = re.findall("\'(.*?)\'", a)

                        if y[0] == datatype and len(time) < 2000000:
    #                         print(row[1])
                            datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                            time.append(datetime_object)
                            data.append(int(a.split(",")[1]))
    #                         print(a)
                        elif y[0] == "signalstrength":
                            datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                            timesignalstrength.append(datetime_object)
                            signalstrength.append(int(a.split(",")[1]))
                        elif len(time) > 2000:
                            print("ecceeded")

l, = plt.plot(time, data, 'o-')



class Index:
    ind = 26
    def next(self, event):
        self.ind += 1
        print("{0:0=2d}".format(self.ind))
        if self.ind > 31:
            self.ind = 1
        with open(path) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            time.clear()
            data.clear()
			
            for row in spamreader:
                     x = re.findall("\((.*?)\)", row[2])
                     if ("-"+"{0:0=2d}".format(self.ind)) in row[1]:
                         for a in x:
                            y = re.findall("\'(.*?)\'", a)

                            if y[0] == datatype and len(time) < 2000000:
        #                         print(row[1])
                                datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                                time.append(datetime_object)
                                data.append(int(a.split(",")[1]))
        #                         print(a)
                            elif y[0] == "signalstrength":
                                datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                                timesignalstrength.append(datetime_object)
                                signalstrength.append(int(a.split(",")[1]))
                            elif len(time) > 2000:
                                print("ecceeded")
#         plt.scatter(time, data)
        ax.axis([min(time), max(time), min(data), max(data)])
        l.set_ydata(data)
        l.set_xdata(time)
#         plt.scatter(timesignalstrength, signalstrength)
#         plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees
        plt.draw()
    def prev(self, event):
          self.ind -= 1
          print("{0:0=2d}".format(self.ind))
          time.clear()
          data.clear()
          with open(path) as csvfile:
                	spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
                	for row in spamreader:
                             x = re.findall("\((.*?)\)", row[2])
                             if ("-"+"{0:0=2d}".format(self.ind)) in row[1]:
                                 for a in x:
                                    y = re.findall("\'(.*?)\'", a)

                                    if y[0] == "ignition" and len(time) < 2000000:
                #                         print(row[1])
                                        datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                                        time.append(datetime_object)
                                        data.append(int(a.split(",")[1]))
                #                         print(a)
                                    elif y[0] == "signalstrength":
                                        datetime_object = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                                        timesignalstrength.append(datetime_object)
                                        signalstrength.append(int(a.split(",")[1]))
                                    elif len(time) > 2000:
                                        print("ecceeded")
          l.set_ydata(data)
          l.set_xdata(time)
          ax.axis([min(time), max(time), min(data), max(data)])
          plt.draw()



callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
plt.xticks(rotation = 90) # Rotates X-Axis Ticks by 45-degrees

plt.show()



