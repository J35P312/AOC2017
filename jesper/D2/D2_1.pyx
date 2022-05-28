from libcpp.vector cimport vector

def main(str infile):

	#in cython, the script gets more efficient if you declare type of variables
	cdef str line
	cdef int minimum
	cdef int maximum
	cdef list numbers

	cdef vector[int] row_diff = []	

	for line in open(infile):
		content=line.strip().split()

		#convert all elements into integer (i.e apply int() to every element)
		numbers=list(map(int,content))

		#find max and min
		minimum=min(numbers)
		maximum=max(numbers)

		#add to c++ style vector!
		row_diff.push_back(maximum-minimum)

	print( sum(row_diff) )
