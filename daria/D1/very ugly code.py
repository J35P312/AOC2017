def main():
    f = open('input.txt') #reading input.txt
    digits = f.read().rstrip() #stripping it of \n 
    
    output = 0
    i = 0 #i - 1st digit
    j = 1 #j - following

    while j <= len(digits) - 1: #so we wouldn't be out of range
        if int(digits[i]) == int(digits[j]):
            output += int(digits[i])
        i += 1 #moving to the next pair
        j += 1 
                
    if int(digits[-1]) == int(digits[0]): #checking the if last == first
        output += int(digits[-1])
    
    return output


print(main())
