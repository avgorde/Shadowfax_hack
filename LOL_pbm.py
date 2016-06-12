import csv
import matplotlib.pyplot as plt

def read_file(fileName):
	rider_ids_pk = {}
	rider_ids_time = {}
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
					schtime = []
					schtime.append(row[4])
					delivertime = []
					if row[5] == "NULL":
						delivertime.append('0')
					else:
						delivertime.append(row[5])
					pickup1 = []
					pickup1.append(row[6])
					pickup1.append(row[7])				
					delivered = []
					delivered.append(row[8])
					delivered.append(row[9])				
					rider_ids_pk[keyname].append(pickup1)
					rider_ids_dl[keyname].append(delivered)
					rider_ids_time[keyname].append([schtime, delivertime])
				else:
					schtime = []
					schtime.append(row[4])
					delivertime = []
					if row[5] == "NULL":
						delivertime.append('0')
					else:
						delivertime.append(row[5])
					pickup1 = []
					pickup1.append(row[6])
					pickup1.append(row[7])				
					delivered = []
					delivered.append(row[8])
					delivered.append(row[9])				
					rider_ids_pk[keyname] = [pickup1]
					rider_ids_dl[keyname] = [delivered]
					rider_ids_time[keyname] = [[schtime, delivertime]]
			counter += 1
	#x_ar = []
	#y_ar = []
	for key in rider_ids_pk.keys():
		print(key, (rider_ids_pk[key])) 
		print(key, (rider_ids_dl[key]))
		print(key, (rider_ids_time[key]))
		sched_info_all = []
		delvr_info_all = []
		for i in range(len(rider_ids_time[key])):
			print(i)
			print(rider_ids_time[key][i][0])
			sched_info, delvr_info = getTime(rider_ids_time[key][i])
			sched_info_all.append(sched_info)
			delvr_info_all.append(delvr_info)

		#for i in range(len(rider_ids_pk[key])):
			#x_ar.append(rider_ids_pk[key][i][0])
			#y_ar.append(rider_ids_pk[key][i][1])
		#distMatr(rider_ids_pk[key], rider_ids_dl[key])
		exit()

def getTime(time_dict):
	"""

	"""
	sched_info = []
	delvr_info = []
	print("In get time function:")#,time_dict)
	print len(time_dict)

	for i in range(len(time_dict)):
		temp_sc = time_dict[i][0].split(" ")
		date_sc = temp_sc[0].split("-")
		year_sc = int(date_sc[0])
		mnth_sc = int(date_sc[1])
		day_sc = int(date_sc[2])
		time_sc = temp_sc[1].split(":")
		hr_sc = int(time_sc[0])
		min_sc = int(time_sc[1])
		sec_sc = int(time_sc[2])
	#	ttime_sc = ()
		sched_info.append([year_sc, mnth_sc, day_sc, hr_sc, min_sc, sec_sc])
		#print(year_sc, mnth_sc, day_sc, hr_sc, min_sc, sec_sc)

		if time_dict[i][1] == 'NULL':
			temp_dl = 'NULL'
			delvr_info.append(['NULL'])
		else:
		#	print(time_dict[1])
			temp_dl = time_dict[i][1].split(" ")
			date_dl = temp_dl[0].split("-")
			year_dl = int(date_dl[0])
			mnth_dl = int(date_dl[1])
			day_dl = int(date_dl[2])
			time_dl = temp_dl[1].split(":")
			hr_dl = int(time_dl[0])
			min_dl = int(time_dl[1])
			sec_dl = int(time_dl[2])
	#		ttime_sc = ()
			#print(year_dl, mnth_dl, day_dl, hr_dl, min_dl, sec_dl)
			delvr_info.append([year_dl, mnth_dl, day_dl, hr_dl, min_dl, sec_dl])
	
	return sched_info, delvr_info	

def distMatr(loc1, loc2):
	"""

	"""
	import numpy as np
	import math

	dist_matr = np.zeros((len(loc1), len(loc2)))

	for i in range(len(loc1)):
		for j in range(len(loc1)):
			dist_matr[i][j] = math.sqrt(math.pow((float(loc1[i][0]) - float(loc2[j][0])),2) + math.pow((float(loc1[i][1]) - float(loc2[j][1])),2))


	for i in range(len(loc1)):
		for j in range(len(loc2)):
			print(dist_matr[i][j]),
		print("\n")

def distMatr1(list1):
	"""

	"""
	import numpy as np
	import math

	#print list1
	print len(list1)
	dist_matr = np.zeros((len(list1), len(list1)))

	for i in range(len(list1)):
		for j in range(len(list1)):
			if i == j:
				print(list1[i], list1[i])
			dist_matr[i][j] = math.sqrt(math.pow((float(list1[i][2]) - float(list1[j][4])),2) + math.pow((float(list1[i][3]) - float(list1[j][5])),2))

	for i in range(len(list1)):
		for j in range(len(list1)):
			print(dist_matr[i][j]),
		print("\n")


def get_cluster(fileName):
	"""
	"""
	cluster_info = {}
	count = 0
	with open(fileName) as inFile:
		csv_file = csv.reader(inFile)
		for row in csv_file:
			if count == 0:
				count += 1
				continue
			else:
				cluster_id = row[3]
				if cluster_id in cluster_info.keys(): 
					cluster_info[cluster_id].append([row[2],row[4],row[5],row[6],row[7],row[8],row[9]])
				else:
					cluster_info[cluster_id]=[[row[2],row[4],row[5],row[6],row[7],row[8],row[9]]]
					#print(cluster_info)
	rider_info={}
	for key, value in cluster_info.items():
		for i in range(len(value)):
#			print(value[i][0])
			rider_id = value[i][0]
			#print rider_id
			if rider_id in rider_info.keys(): 
				rider_info[rider_id].append([value[i][1],value[i][2], value[i][3],value[i][4],value[i][5],value[i][6]])
			else:
				#rider_info[rider_id]=[[value[1:]]]
				rider_info[rider_id]=[[value[i][1],value[i][2], value[i][3],value[i][4],value[i][5],value[i][6]]]

	for key, value in rider_info.items():
		sched_info, delvr_info = getTime(value)
		print(key)

		distMatr1(value)

		#"""
		for i in range(len(delvr_info)):
			#print("#########",delvr_info[i][0])
			if delvr_info[i][0] == 'NULL':
				continue
			else:
				temp = delvr_info[i][2]
				#print "temp",temp
				if delvr_info[i][2] == temp:
					print(sched_info[i], delvr_info[i])
					print(find_time(sched_info[i], delvr_info[i]))
		#"""
		exit()
		#print(sched_info)
		#print(delvr_info)

def find_time(stime, etime):
	"""

	Args:
	    stime:
	    etime:

	Returns:

	"""
	time_t = []
	for i in range(len(stime)):
		time_t.append((stime[i]-etime[i]))

	return time_t

if __name__ == "__main__":
	
	import os
	
	data_path = r"/home/shree/Desktop/Shadowfax"
	csvfile = "orderdata.csv"
	csvpath = os.path.join(data_path, csvfile)
	#read_file(csvpath)
	get_cluster(csvpath)
