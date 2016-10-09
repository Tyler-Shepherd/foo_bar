

def try_all_adjacent(pos, num_traveled, traveled, maze, removed_wall):
    if pos == [len(maze)-1, len(maze)-1]:
        return num_traveled


    print pos, num_traveled, traveled


    right = [pos[0]+1,pos[1]]
    left = [pos[0]-1,pos[1]]
    up = [pos[0], pos[1]-1]
    down = [pos[0], pos[1]+1]
    
    path_lengths = []
    
    if right[0]<len(maze) and right not in traveled:
    	if maze[right[0]][right[1]] == 0:
        	traveled.append(right)
        	path_lengths.append(try_all_adjacent(right, num_traveled+1, traveled, maze, removed_wall))
        	traveled.pop()
       	elif not removed_wall:
       		traveled.append(right)
        	path_lengths.append(try_all_adjacent(right, num_traveled+1, traveled, maze, True))
        	traveled.pop()
        
    if left[0]>=0 and left not in traveled:
        if maze[left[0]][left[1]] == 0:
        	traveled.append(left)
        	path_lengths.append(try_all_adjacent(left, num_traveled+1, traveled, maze, removed_wall))
        	traveled.pop()
       	elif not removed_wall:
       		traveled.append(left)
        	path_lengths.append(try_all_adjacent(left, num_traveled+1, traveled, maze, True))
        	traveled.pop()
        
    if up[1]>=0 and up not in traveled:
    	if maze[up[0]][up[1]] == 0:
        	traveled.append(up)
        	path_lengths.append(try_all_adjacent(up, num_traveled+1, traveled, maze, removed_wall))
        	traveled.pop()
       	elif not removed_wall:
       		traveled.append(up)
        	path_lengths.append(try_all_adjacent(up, num_traveled+1, traveled, maze, True))
        	traveled.pop()
        
    if down[1]<len(maze) and down not in traveled:
    	if maze[down[0]][down[1]] == 0:
        	traveled.append(down)
        	path_lengths.append(try_all_adjacent(down, num_traveled+1, traveled, maze, removed_wall))
        	traveled.pop()
       	elif not removed_wall:
       		traveled.append(down)
        	path_lengths.append(try_all_adjacent(down, num_traveled+1, traveled, maze, True))
        	traveled.pop()

    if len(path_lengths)==0:
        return 9999999999999

    return min(path_lengths)



def answer(maze):
    # your code here
    
    pos = [0,0]
    num_traveled = 1
    traveled = [[0,0]]

    #path_lengths = []

    # for row in range(0,len(maze)):
    # 	for col in range(0,len(maze)):
    # 		if maze[row][col] == 1:
    # 			maze[row][col] = 0
    # 			path_lengths.append(try_all_adjacent(pos, num_traveled, traveled, maze))
    # 			maze[row][col] = 1

    # if len(path_lengths) == 0:
    # 	return try_all_adjacent(pos, num_traveled, traveled, maze)

    # return min(path_lengths)
    return try_all_adjacent(pos, num_traveled, traveled, maze, False)
    

#print answer([[0,1,1], [1,1,1], [1,1,0]])
#print answer([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])