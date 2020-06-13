import csv
import numpy
filename = 'pima-indians-diabetes.data.csv'# ensure that you have downloaded the directory
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)