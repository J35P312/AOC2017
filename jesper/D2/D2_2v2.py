#this function will divide every number in a list by ever number in the same list.
#it will return the result of a division that gives a whole number (i.e integer)

def all_versus_all(numbers):
	
	for i in numbers:
		for j in numbers:

			#only compare different numbers
			if i == j:
				continue

			#skip if i < j:
			if i < j:
				continue

			res= i/j	

			#check if the result is an even number
			if i % j == 0:	
				return( int(res) )

result = 0	
#read the file line by line
for line in open("input.txt"):
	content=line.strip().split()
	
	numbers=[]
	#convert all elements into integer (i.e apply int() to every element)
	for value in content:
		numbers.append( int(value) )

	result += all_versus_all(numbers)
					
print( result )
