import pandas as pd

#here you generate column names a,b,c,d....p since you dont use these, you may skip
#colnames = list(map(chr, range(ord('a'), ord('p')+1)))

#open csv, skip header
my_df = pd.read_csv('input.txt', sep = '\t', header=None)

#print(my_df)

#generate a "list" of all  maxmimum values (line), first value will correspond to first line, second to second line etc
max_element = my_df.max(axis=1)

#essentially you do this, i is the line number, line is the line itself
max_element=[]
for i, line  in my_df.iterrows():
	max_element.append( max( line ) ) 

#generate a "list" of all minimum values( per line, first value will correspond to first line, second to second line etc
min_elememt = my_df.min(axis=1)

#generate a new "list", such that each element corresponds to the difference between per row max and min (i.e diff[i] = max_element[i] - min_element[i])
#diff = max_element - min_elememt

#more old school solution
diff=[]
for i in range(0,len(min_elememt)):
	diff.append( max_element[i] - min_elememt[i] )

#sum all differences
print( sum(diff) )

