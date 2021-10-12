import matplotlib.pyplot as plt
import math

files = ["sources/001.dat", "sources/002.dat", "sources/003.dat", "sources/004.dat", "sources/005.dat"]

def parser(filename):
	x = []
	y = []
	data = []
	with open(filename) as f:
		data = f.read().split('\n')

	for i in range(1, len(data)):
		data[i] = (data[i]).split(' ')

	n = int(data[0])
	data = data[1:]

	for i in range(n):
		x.append(float(data[i][0]))
		y.append(float(data[i][1]))
	data = [x, y, n]

	return data
    
for i in range(len(files)):
	data = parser(files[i])
	fig, axs = plt.subplots()
	axs.scatter(data[0], data[1], s = 12 - 2*i)
	axs.axis('equal')
	plt.title("Number of points: " + str(data[2]))
	
	fig.savefig(str(i+1) + ".png")
	

    
    
