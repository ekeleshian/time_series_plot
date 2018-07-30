
from matplotlib import pyplot
import csv
from datetime import datetime

database = 'daily-minimum-temperatures-in-me.csv'

wanted_data = []
x_axis = []
y_axis = []

with open(database, newline = '') as csvfile:
	reader = csv.reader(csvfile)
	for l in reader:
		for i in l:
			wanted_data.append(i)

wanted_data.pop()
wanted_data.pop()
wanted_data.pop()

wanted_data = wanted_data[3:]

for i in wanted_data:
	i = i.split(';')
	x_axis.append(datetime.strptime(i[0], '%Y-%m-%d'))
	if '?' in i[1]:
		y_axis.append(str(i[1][1:]))
	else:
		y_axis.append(str(i[1]))

pyplot.scatter(x_axis, y_axis)
pyplot.show()
