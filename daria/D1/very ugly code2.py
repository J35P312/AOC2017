def main():
    f = open('input.txt') #reading input.txt
    digits = f.read().rstrip() #stripping it of \n

    output = 0
    steps = int(len(digits)/2)

    i = 0  
    while i < steps:
        j = i + steps
        if int(digits[i]) == int(digits[j]):
            output += int(digits[i])
        i += 1

    i = steps
    while i < len(digits):
        j = i - steps
        if int(digits[i]) == int(digits[j]):
            output += int(digits[i])
        i += 1 

    
    return output


print(main())

