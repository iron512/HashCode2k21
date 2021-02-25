#!/usr/bin/python

import sys
import os
import math 
import numpy as np

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def solution(handler):
	output = open("../outputs/" + handler.name.replace("../inputs","")[1] + "_exec.out", "w")

	#Write here the solution
	first = handler.readline()
	first = first.replace("\n","").split(" ")

	symTimeCount = first[0]
	intersectionCount = first[1]
	streetCount = first[2]
	carsCount = first[3]
	pointsCount = first[4]

	streets = []
	cars = []

	carTrips = {}
	intersectionMap = {}
	roadMap = {}

	for line in handler.readlines():
		if int(len(streets)) != int(streetCount):		
			line = line.replace("\n","").split(" ")
			streets.append(tuple(line))
			carTrips[line[2]] = 0

			if line[1] not in intersectionMap:
				intersectionMap[line[1]] = []
			intersectionMap[line[1]].append(line[2])
			roadMap[line[2]] = line[3]

		else:
			line = line.replace("\n","").split(" ")
			cars.append(tuple(line))
			for sample in line[1:]:
				carTrips[sample] = carTrips[sample] + 1


	print(roadMap)

	intersCount = 0
	for intersect in intersectionMap:
		#output.write(intersect + "\n")
		#output.write(str(len(intersectionMap[intersect])) + "\n")
		
		tmpCount = 0
		tmp = ""

		for elem in intersectionMap[intersect]:
			if math.ceil(carTrips[elem]) != 0:
				tmpCount = tmpCount+1;
			#output.write(str(elem) + " 1\n")
		
		if tmpCount != 0:
			intersCount += 1;

	output.write(str(intersCount) + "\n")

	for intersect in intersectionMap:
		#output.write(intersect + "\n")
		#output.write(str(len(intersectionMap[intersect])) + "\n")

		tmpCount = 0
		tmp = ""

		newArray = []
		for elem in intersectionMap[intersect]:
			tup = (carTrips[elem],elem)
			newArray.append(tup)
		
		newArray = sorted(newArray, reverse=True)

		trafficLight = 8

		for key,elem in newArray:
			if math.ceil(carTrips[elem]/5) != 0:
				#tmp = tmp + str(elem) + " " + str(int(max(1,trafficLight)))+"\n"
				#trafficLight = trafficLight/2
				tmp = tmp + str(elem) + " " + str(math.ceil(carTrips[elem])/10)+"\n"
				tmpCount = tmpCount+1;
			#output.write(str(elem) + " 1\n")

		if tmpCount != 0:
			output.write(intersect + "\n" + str(tmpCount) + "\n" + tmp)

	output.close()


#--- MAIN ---
inputs = []

print(bcolors.YELLOW + "	PYTHON" + bcolors.RESET)
print()

print("Loading files from inputs directory:\n") 
for row in sorted(os.listdir("../inputs/")):
	row = row.replace("\n","")
	print("	- " + row)
	inputs.append(open("../inputs/"+row,"r"))

print()
#Inputs contains all the input files, lets see on which apply the algorithm
run = []
for decision in sys.argv[1:]:
	run.append(int(decision))

if len(run) != len(inputs):
	print("Wrong argument count")
	sys.exit(1)

for i in range(0,len(inputs)):
	if (run[i] == 1):
		print("(1) Running algs on: " + bcolors.GREEN + inputs[i].name.split("/")[-1] + bcolors.RESET)
		solution(inputs[i])
	else:
		print("(0) Not running algs on: " + bcolors.RED + inputs[i].name.split("/")[-1] + bcolors.RESET)

print()
