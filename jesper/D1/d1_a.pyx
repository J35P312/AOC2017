def main(str infile):

	for line in open(infile):
		captcha=line.strip()
		break

	cdef int i
	cdef list matching = []
	cdef score = 0

	for i in range(0,len(captcha)-1):
		if captcha[i] == captcha[i+1]:
			matching.append( captcha[i] )
			score= int(captcha[i]) + score

	if captcha[-1] == captcha[0]:
		matching.append( captcha[-1] )
		score= int(captcha[-1]) + score

	print(score )
