with open('input.txt') as file:
    maze = []
    for line in file:
        maze.append(int(line))
        
steps = 0
i = 0

while i < len(maze):
    if maze[i] >= 3:
        maze[i] -= 1
        i = i + maze[i] + 1
        steps += 1
    else:
        maze[i] += 1
        i = i + maze[i] - 1
        steps += 1
    
print(steps)
   
