import math

file = open('input.txt', 'r')
result = 0

for line in file:
    amount = 0
    splitted = line.split()

    combos = math.comb(len(splitted), 2)
    
    for i in range(len(splitted)):
        for j in range(i+1, len(splitted)):
            if sorted(splitted[i]) != sorted(splitted[j]):
                amount += 1
       

    if amount == combos:
        result += 1

        
print(result)
