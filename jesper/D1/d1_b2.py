import sys

def main(infile):

	for line in open(infile):
		captcha=line.strip()
		break

	score = 0
	captcha_len=len(captcha)
	steps=int(captcha_len/2)

	#make a longer list, then we do not need to care about circular behaviour of the input	
	double_captcha=captcha+captcha

	for i in range(0,len(captcha)):

		#find position in the longer list
		pos_matching=i+steps

		if captcha[i] == double_captcha[pos_matching]:
			score= int(captcha[i]) + score

	print(score)

main(sys.argv[1])
