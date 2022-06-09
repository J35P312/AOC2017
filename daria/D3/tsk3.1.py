import math

def main(n):
    sq = int(math.ceil(math.sqrt(n)))
    if sq % 2 == 0:
        sq += 1
        
    side_max = [sq*sq - k*(sq-1) for k in range(5)]

    for p in side_max:
        dist = abs(p - n)

        if dist <= (sq-1)//2:
            print(sq-1-dist)
            break

main(312051)
main(361527)
main(12)
main(23) 
