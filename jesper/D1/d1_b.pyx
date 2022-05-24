def main(str infile):

	for line in open(infile):
		captcha=line.strip()
		break

	cdef int i
	cdef int score = 0
	cdef int captcha_len=len(captcha)
	cdef int steps=captcha_len/2

	for i in range(0,len(captcha)):

		pos_matching=i+steps


		if pos_matching > captcha_len-1:
			pos_matching=pos_matching-captcha_len

		if captcha[i] == captcha[pos_matching]:
			score= int(captcha[i]) + score

	print(score)
