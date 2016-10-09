def answer(pegs):
    # your code here

    radii = []
    
    for radius_one in range(1, pegs[1]-pegs[0]-1):
    	radii.append(radius_one)

        next_radius = pegs[1] - radius_one - pegs[0]
        
        radii.append(next_radius)

        for i in range(2, len(pegs)):
            next_radius = pegs[i] - next_radius - pegs[i-1]

            radii.append(next_radius)
        
        print(radii)

        if 2*next_radius == radius_one:
            return radius_one

        radii = []
    
    return [-1,-1]

print answer([4, 17, 50])


