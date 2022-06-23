
#return index of highest number
def find_highest(l):
	m=max(l)
	for i in range(0,len(l)):
		if l[i] == m:
			return(i)

#represent the state as string
def find_state(l):
	s=list( map(str,l) )
	return("-".join(s))

#redistribute blocks	
def update_memory(memory,i):
	blocks=memory[i]
	memory[i]=0
	i+=1
	if i == len(memory):
		i=0

	for b in range(0,blocks):

		memory[i]+=1
		i+=1
		if i == len(memory):
			i=0

	
	return(memory)


memory=[]
for line in open("input.txt"):
	memory = list(map(int,line.strip().split()))

#memory=[0,2,7,0]

states=set([])
states.add( find_state(memory) )

n=0
while True:
	n+=1

	#find the position of highest number
	i=find_highest(memory)

	#redistribute stuff
	memory=update_memory(memory,i)

	#represent current state as a string
	state=find_state(memory)

	#check if current state has been seen
	if state in states:
		break

	#add current state to set
	states.add(state)

print(n)
