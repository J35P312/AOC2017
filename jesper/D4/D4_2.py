v=0
for line in open("input.txt"):
	words=line.strip().split()
	char_dict=[]
	
	for w in words:
		#add empty dictionary to the list
		char_dict.append({})

		#count the number of occurances of each letter
		for letter in w:
			char_dict[-1][letter]=w.count(letter)

	anagram=False
	#search for anagrams
	for i in range(len(char_dict)):

		for j in range(len(char_dict)):
			
			if i == j:
				continue
			#the words must contain the same letters
			if not set(char_dict[j].keys()) == set(char_dict[i].keys() ):
				continue

			anagram=True
			# if the words contains the same letters, we must check if the number of each letter is the same
			for l in char_dict[i]:
				if char_dict[j] != char_dict[i]:
					anagram=False
	if anagram:
		continue
			
	v+=1


print(v)	
