def main():
    f = open('input.txt') #reading input.txt
    digits = f.read().rstrip() #stripping it of \n

    output = 0
    steps = int(len(digits)/2)

    #range function will generates numbers 0,1,2..... len(digits-1), i will take each value
    for i in range(0,len(digits)):

        #essentially your first loop
        if i < steps:
            j=i+steps
        #your second loop
        else:
            j=i-steps
        
        if int(digits[i]) == int(digits[j]):
            output += int(digits[i])
    
    return output


print(main())

