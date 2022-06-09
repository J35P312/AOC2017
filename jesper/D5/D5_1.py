instructions=[]
for line in open("input.txt"):
	instructions.append( int(line.strip()) )

pos=0
steps=0
while True:
	jump=instructions[pos]
	instructions[pos]+=1
	pos=pos+jump
	steps+=1

	if pos > len(instructions)-1 or pos < 0:
		break



print(steps)
