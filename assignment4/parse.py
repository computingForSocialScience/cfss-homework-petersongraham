import csv
import sys

print sys.argv[0]


def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
	return(lines)

hydepark = readCSV('permits_hydepark.csv')

import math

def get_avg_latlng(csvlist):
	latitude = [item[128] for item in hydepark]
	longitude = [item[129] for item in hydepark]
	lat_list = []
	long_list = []
	
	for i in range(len(latitude)) and range(len(longitude)):
		lat_flt = float(latitude[i])
		long_flt = float(longitude[i])
		lat_list.append(lat_flt)
		long_list.append(long_flt)
	
	avlat = sum(lat_list)/float(len(latitude))
	avlong = sum(long_list)/float(len(longitude))
		
	print avlat, avlong


import numpy as np
import matplotlib.pyplot as plt


from matplotlib import pyplot as plt
import Image

def zip_code_barchart(sirmixalot):
    zipcodes = []
    for i in sirmixalot:
    	if i[27] != "NJ":
    		for column in (28, 35, 42, 49, 56, 63, 70, 84, 91, 98, 105, 112, 119, 126):
    			if i[column] != '':
    				zipcodes.append(i[column][0:5])

    zipcodes_int = []
    for code in zipcodes:
    	zipcodes_int.append(int(code))

    plt.hist(zipcodes_int, bins=200)
    plt.xlabel('Contractor Zipcodes')
    plt.ylabel('Frequency')
    plt.title('Zipcode Histogram for City of Chicago Contractors')
    plt.grid(True)
    plt.draw()
    plt.savefig('histogram.png')
    Image.open('histogram.png').save('histogram.jpg', 'JPEG')

if sys.argv[1] == 'latlong':
    get_avg_latlng(hydepark)
elif sys.argv[1] == 'hist':
    zip_code_barchart(hydepark)

