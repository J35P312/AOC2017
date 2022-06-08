import math

def main(n):
    sq = round(math.sqrt(n)) + 2 
    side_max = [sq*sq - k*(sq-1) for k in range(5)]

    for p in side_max:
        dist = abs(p - n)

    if dist < (sq-1)//2:
        print(sq-1-dist)
    else:
        print(dist)

main(312051)
main(361527)
main(12)
main(23) #that doesnt work
