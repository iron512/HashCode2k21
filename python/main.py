#!/usr/bin/python

import sys
import os


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

	for line in handler.readlines():
		if int(len(streets)) != int(streetCount):		
			streets.append(tuple(line.replace("\n","").split(" ")))
		else:
			cars.append(tuple(line.replace("\n","").split(" ")))

	print(streets[0])
	print(cars[0])
	
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
