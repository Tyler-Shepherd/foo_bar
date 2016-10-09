def answer(pegs):
	radius_one = -1 * pegs[0]

	modifier = 2

	for peg in range(1,len(pegs)-1):
		radius_one += modifier*pegs[peg]

		modifier *= -1

	radius_one += modifier/2 * pegs[len(pegs)-1]

	radius_one *= 2

	if radius_one <= 0:
		return [-1,-1]
	elif len(pegs)%2==0:
	    if radius_one%3 == 0:
	        return [radius_one/3, 1]
	    return [radius_one, 3]
	else:
		return [radius_one,1]

x = 1
print x*1.0/3