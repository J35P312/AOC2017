import numpy
import math



#the input
#target=312051
target=16

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

#Now we know the layer of our target, next we will find its position within a row in the outer layer

#make lists containing all numbers in the rows of the outer layers:
right_row=list(range(current_max[-2]+1,current_max[-2]+row_length[-1]))
upper_row=list(range(current_max[-2]+row_length[-1]-1,current_max[-2]+2*row_length[-1]-1  ))
left_row=list(range(current_max[-2]+row_length[-1]+row_length[-1]-2,current_max[-2]+3*row_length[-1]-2))
lower_row=list(range(current_max[-2]+3*row_length[-1]-3,current_max[-2]+4*row_length[-1]-3))

pos=0
#check which list contains our target:
if target < current_max[-2]+row_length[-1]:
	print("right")
	for i in range(0,len(right_row)):
		if right_row[i] == target:

			if i == math.ceil(len(right_row)/2):
				pos=0
			elif i <= math.ceil(len(right_row)/2):
				pos=math.ceil(len(right_row)/2)-i-1
			else:
				pos=i-math.ceil(len(right_row)/2)



elif target < current_max[-2]+2*row_length[-1]-1:
	print("upper")
	for i in range(0,len(upper_row)):
		if upper_row[i] == target:

			if i == math.ceil(len(upper_row)/2):
				pos=0
				print("hej")
			elif i <= math.ceil(len(upper_row)/2):
				pos=math.ceil(len(upper_row)/2)-i
			else:
				pos=1+i-math.ceil(len(upper_row)/2)

	
elif target < current_max[-2]+3*row_length[-1]-2:
	print("left")
else:
	print("lower")

#number of layers
print(math.ceil(len(current_max)/2))
#element within outer layer
print(pos)
#distance
print(pos+math.ceil(len(current_max)/2))
