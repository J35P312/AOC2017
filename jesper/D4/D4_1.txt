v=0
for line in open("input.txt"):
	words=line.strip().split()
	#set is a python datastructure, it is like a mathematical set, containing only unique entries; compared to list, set is unordered, and cannot be indexed
	unique_words=set(words)
	if len(words) == len(unique_words):
		v+=1

print(v)
		
