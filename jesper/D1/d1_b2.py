import sys

def main(infile):

	for line in open(infile):
		captcha=line.strip()
		break

	score = 0
	captcha_len=len(captcha)
	steps=int(captcha_len/2)

	double_captcha=captcha+captcha

	for i in range(0,len(captcha)):

		pos_matching=i+steps

		if captcha[i] == double_captcha[pos_matching]:
			score= int(captcha[i]) + score

	print(score)

main(sys.argv[1])
