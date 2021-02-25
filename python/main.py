#!/usr/bin/python

import sys
import os


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def solution(handler):
	#Write here the solution
	output = open("../outputs/" + handler.name.replace("../inputs","")[1] + "_exec.out", "w")

	for line in handler.readlines():
		output.write(line)
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
