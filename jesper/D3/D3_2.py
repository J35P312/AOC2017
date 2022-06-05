import numpy
import math

#find the new value of an element, by adding all surrounding values to it
def find_value(arr,x,y,target):
	v=0

	for i in range(-1,2):
		for j in range(-1,2):
					
			#negative values means we are looking outside of array
			if x+i < 0 or y+j < 0:
				continue

			#we need try, or the program will crash when we look outside of the array
			try:
				v+=arr[x+i][y+j]
			except:		
				pass

	#the value of element is larger than our target/input, print it and quit
	if v > target:
		print("res")
		print(v)
		quit()

	return(v)

#we go along the edges and update
def traverse_edge(arr, l,target):

	#analyse right side	
	for i in reversed(range(l-1)):
		arr[i][l-1]=find_value(arr,i,l-1,target)

	#analyse top
	for i in reversed(range(1,l-1)):
		arr[0][i]=find_value(arr,0,i,target)

	#analyse left side
	for i in range(l):
		arr[i][0]=find_value(arr,i,0,target)

	#analyse bottom
	for i in range(1,l):
		arr[l-1][i]=find_value(arr,l-1,i,target)

	return(arr)

#the input
target=312051

#the array starts with [1]
arr=numpy.ones([1,1])

while True:
	#add zeros around the array (ie make room for a new layer
	arr=numpy.pad(arr,[1,1])
	print(len(arr))

	#go around the edges (i.e populate the new layer)
	arr=traverse_edge(arr,len(arr),target)
	print(arr)


print(v)
