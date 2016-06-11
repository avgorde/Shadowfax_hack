import csv
import matplotlib.pyplot as plt

def read_file(fileName):
	rider_ids_pk = {}
	rider_ids_dl = {}
	counter = 0
	with open(fileName, 'r') as inFile:
		c_reader = csv.reader(inFile)
		for row in c_reader:
			if counter == 0:
				index = row[1]
			else:
				keyname = row[2]
				if keyname in rider_ids_pk.keys():
	
					pickup1 = []
					pickup1.append(row[6])
					pickup1.append(row[7])				
					delivered = []
					delivered.append(row[8])
					delivered.append(row[9])				
					rider_ids_pk[keyname].append(pickup1)
					rider_ids_dl[keyname].append(delivered)
				else:
					pickup1 = []
					pickup1.append(row[6])
					pickup1.append(row[7])				
					delivered = []
					delivered.append(row[8])
					delivered.append(row[9])				
					rider_ids_pk[keyname] = [pickup1]
					rider_ids_dl[keyname] = [delivered]
			counter += 1
	x_ar = []
	y_ar = []
	for key in rider_ids_pk.keys():
		print(key, (rider_ids_pk[key])) 
		print(key, (rider_ids_dl[key]))
		for i in range(len(rider_ids_pk[key])):
			x_ar.append(rider_ids_pk[key][i][0])
			y_ar.append(rider_ids_pk[key][i][1])
		distMatr(rider_ids_pk[key], rider_ids_dl[key])
		exit()

def distMatr(loc1, loc2):
	"""

	"""
	import numpy as np
	import math

	dist_matr = np.zeros((len(loc1), len(loc2)))

	for i in range(len(loc1)):
		for j in range(len(loc1)):
			if i == j:
				print(loc1[i], loc2[i])
			dist_matr[i][j] = math.sqrt(math.pow((float(loc1[i][0]) - float(loc2[j][0])),2) + math.pow((float(loc1[i][1]) - float(loc2[j][1])),2))	


	for i in range(len(loc1)):
		for j in range(len(loc2)):
			print(dist_matr[i][j]),
		print("\n")
if __name__ == "__main__":
	
	import os
	
	data_path = r"/home/shree/Desktop/Shadowfax"
	csvfile = "orderdata.csv"
	csvpath = os.path.join(data_path, csvfile)
	read_file(csvpath)
