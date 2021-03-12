# HashCode2021

This is the (un)official repository of the **Never gonna heap you up** italian team. We will post our up-to-date solution only after the conlusion of the competition. We are 4 students of the university of trento and we race under out **university hub**. 

## Strategy (which won't work as planned of course).

Since the time is limited and we rely only on heuristics on and the infamous *botta de culo* technique (not necessarily in this exact order) we planned a dual language solution.
We are going to use **python** to develop a fast solution and probably preprocess some data, then, if we got the correct dip we will try to improve the solution using **C++**. Here you can found the starting environment that we are going to use.


## Setup

Python requires a little setup.
Generate a the virtual environment for python.

`
$	cd python
`

`
$	pyhton3 - m venv virtual
`

Activate it and install the environmental requirements.

`
$ 	. virtual/bin/activate
`

`
$	pip install -r requirements.txt
`

## Run

`
$ 	python3 main.py 0 1 0 1 1
`

## Website

You can follow the updates on the competition and after, about us on our website.

https://www.thisworldthesedays.com/nevergonnaheap1.html

## Updates

- During the competition we opted for using just python. The time is scarce and our algorithm took just a few second per each input, so the due to further modification, the cpp version is not supported. The original code is still present.
- The code is a little messy. It has not been modified from our last submission.
- We got great results. The top team score was 10,586,135, while ours was 9,551,800. We ended up 4th in our *university*, 16th in *Italy* and 423 *All over the world* (better than 95% of registered teams)