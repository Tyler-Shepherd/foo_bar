
# Problem: Given a grid, find the shortest path distance from upper left corner to bottom right corner
# Spaces with a 1 cannot be passed, spaces with a 0 can
# Up to one wall can be removed

# Basically uses Dijkstra's method to search for shortest path

# Runtime complexity: O(h*w*n), where h is grid height, w is grid width
# and n is number of walls

# Space complexity: O(h*w)

# Gets the minimum distance of all unvisited spaces
# Or returns None if no remaining locations unvisited and
# have a viable path
def get_min_dist(distances, visited):
	min_dist = 999999999
	min_pos = None

	for x in range(0,len(distances)):
		for y in range(0,len(distances[0])):
			if visited[x][y] == 0:
				if distances[x][y] < min_dist:
					min_dist = distances[x][y]
					min_pos = [x, y]

	return min_pos

# Returns the shortest possible distance given a maze
# or "infinity" if not possible
def get_shortest(maze):

    # Essentially infinity in this problem
    infinity = 999999999

    distances = []
    visited = []

    for row in maze:
    	new_row = []
    	visited_row = []
    	for col in row:
    		new_row.append(infinity)
    		visited_row.append(0)
    	distances.append(new_row)
    	visited.append(visited_row)

    distances[0][0] = 1

    current = [0,0]

    while True:

    	if current[0]==len(maze)-1 and current[1]==len(maze[0])-1:
    		return distances[len(maze)-1][len(maze[0])-1]

    	right = [current[0]+1, current[1]]
    	left = [current[0]-1, current[1]]
    	up = [current[0], current[1]-1]
    	down = [current[0], current[1]+1]

    	current_dist = distances[current[0]][current[1]]

        # Sorry for the repetitious code, could be cleaned up

    	if right[0] < len(maze) and visited[right[0]][right[1]]==0:
    		if maze[right[0]][right[1]] == 0:
    			if current_dist + 1 < distances[right[0]][right[1]]:
    				distances[right[0]][right[1]] = current_dist + 1

    	if left[0] >= 0 and visited[left[0]][left[1]]==0:
    		if maze[left[0]][left[1]] == 0:
    			if current_dist + 1 < distances[left[0]][left[1]]:
    				distances[left[0]][left[1]] = current_dist + 1

    	if up[1] >= 0 and visited[up[0]][up[1]]==0:
    		if maze[up[0]][up[1]] == 0:
    			if current_dist + 1 < distances[up[0]][up[1]]:
    				distances[up[0]][up[1]] = current_dist + 1

    	if down[1] < len(maze[0]) and visited[down[0]][down[1]]==0:
    		if maze[down[0]][down[1]] == 0:
    			if current_dist + 1 < distances[down[0]][down[1]]:
    				distances[down[0]][down[1]] = current_dist + 1

    	visited[current[0]][current[1]] = 1

    	current = get_min_dist(distances, visited)
    	if current == None:
    		return infinity

def answer(maze):
	shortest_paths = []

    # Not the most optimal algorithm here, as it simply
    # attempts removing every wall and seeing if that is a possible solution
	for x in range(0,len(maze)):
		for y in range(0, len(maze[0])):
			if maze[x][y]==1:
				maze[x][y] = 0
				shortest_paths.append(get_shortest(maze))
				maze[x][y] = 1

	return min(shortest_paths)