#list that store the difference between maximum and minimum column in each row
row_diff=[]

#read the file line by line. The loop starts from first line, and ends on the last; one line per itteration
for line in open("input.txt"):

	#remove endline charachter
	line=line.strip()
	#split the line at each whitespace i.e space or tab, the result is a list of strings, each element correspond to a column
	content=line.split()

	numbers=[]
	#convert the strings to int
	for value in content:
		numbers.append( int(value) )

	#find the minimum value in numbers
	minimum=min(numbers)

	#find maximum value
	maximum=max(numbers)

	#store the difference in a list
	row_diff.append( maximum-minimum )

#sum up all the differences, and print
print( sum(row_diff) )
