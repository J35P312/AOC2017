#weigth of each program
w={}

#store every program that each program is carrying i.e {"A":{B,C} } : A -> B,C
c={}

#store all the stuff
for line in open("input.txt"):

	content=line.strip().split()
	word=content[0]
	weight=content[1].strip("()")

	w[word]=int(weight)
	c[word]=set([])

	#the program is not carrying any program
	if not "->" in line:
		continue

	carried=line.split("-> ")[-1].replace(",","").split()

	#add all carried programs into a set
	for e in carried:
		c[word].add(e)

connected=set([])
for word in c:

	#if a program is carried by another program, it is not the bottom
	for conn in c[word]:
		connected.add(conn)

	#the bottom must carry something
	if not c[word]:
		connected.add(word)
	
print( set(c.keys())-connected  )
