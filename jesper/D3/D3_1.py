import numpy
import math



#the input
target=312051
#target=1024

#we start with a box of one layer, and add layers until the box contain our target.
#Each time we add a layer the number of elements in the box will grow with n*4+4, n is the length of the box of current layer.
#the number of layers in this box will correspond to our x or y coordinate

#the highest possible value in a box with current number of layers (start from 1)
current_max=[1]

#the lenght of the box
row_length=[1]

#find the layer where our target lives
while current_max[-1] < target:

	#add the maximum value of the current layer
	current_max.append( (row_length[-1]*4+4)+current_max[-1] )

	#add two for the new "corners"
	row_length.append(row_length[-1]+2)


#the position of the 1, i.e the middle of the matrix
one=math.ceil(row_length[-1]/2)
print(one)

#Now we know the layer of our target, next we will find its position within a row in the outer layer

#make lists containing all numbers in the rows of the outer layers:
right_row=list(range(current_max[-2]+1,current_max[-2]+row_length[-1]))
upper_row=list(range(current_max[-2]+row_length[-1]-1,current_max[-2]+2*row_length[-1]-1  ))
left_row=list(range(current_max[-2]+row_length[-1]+row_length[-1]-2,current_max[-2]+3*row_length[-1]-2))
lower_row=list(range(current_max[-2]+3*row_length[-1]-3,current_max[-2]+4*row_length[-1]-3))

#check which list contains our target:
if target < max(right_row):
	#the target is on the right side
	print("right")
	x=row_length[-1]

	for i in range(0,len(right_row)):
		if right_row[i] == target:
			y=i+2

elif target < max(upper_row):
	#target is on the upper side
	print("up")
	y=row_length[-1]
	
	for i in range(0,len(upper_row)):
		if upper_row[i] == target:
			x=i+1

elif target < max(left_row):
	#target is on the left side
	print("left")
	x=1
	
	for i in range(0,len(left_row)):
		if left_row[i] == target:
			y=i+1

else:
	#target is on the bottom
	y=1	
	for i in range(0,len(lower_row)):
		if lower_row[i] == target:
			x=i+1


#number of layers
print(math.ceil(len(current_max)/2))
#manhattan distance
print( abs(x-one)+abs(y-one) )
