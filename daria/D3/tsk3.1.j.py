import math

def main(n):
    #remember to round up, if you round down, the matrix size gets too small!
    sq = int( math.ceil(math.sqrt(n)) )

    #our matrix is always an odd number long, if it is even, you must
    #add one, or the spiral wont fit!
    if not sq % 2:
       sq +=1

    #print(sq,"sq")

    side_max = [sq*sq - k*(sq-1) for k in range(5)]

    for p in side_max:
        dist = abs(p - n)

        if dist <= (sq-1)//2:
            print(sq-1-dist)
            break
        #else:
        #    print(dist)

main(312051)
main(361527)
main(12)
main(23) #that doesnt work; now it does =P


