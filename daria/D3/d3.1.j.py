import math
n=23

current_max=[1]
row_length=[1]

#find the layer where our target lives
while current_max[-1] < n:

	#add the maximum value of the current layer
	current_max.append( (row_length[-1]*4+4)+current_max[-1] )

	#add two for the new "corners"
	row_length.append(row_length[-1]+2)

sq = row_length[-1]
print(sq)
pivots = [sq*sq - k*(sq-1) for k in range(5)]

for p in pivots:
    dist = abs(p - n)
    print(dist)
    if dist <= (sq-1)//2:
        print(sq-1-dist)
        break
