
from collections import deque
def bfsPath(grid,startChar='S',goalChars='Z',wallChar='#'):
    def bfs(startstate):
        frontier =  deque([startstate])
        prev = {startstate:None}
        while frontier:
            x, y = frontier.popleft()  
            if grid[x][y] in goalChars:
                return prev, (x,y)
            for xd, yd in dirs:
                x1 = x + xd
                y1 = y + yd
                if 0 <= x1 < height and 0 <= y1 < width and grid[x1][y1] != wallChar:
                    if (x1,y1) not in prev:
                        frontier.append((x1,y1))
                        prev[(x1,y1)] = (x,y)
        return None, None
    
    def reconstructPath(prev,goalstate):
        state = goalstate
        path = []
        while state is not None:
            path.append(state)
            state = prev[state]
        path.reverse()
        return path

    dirs = [(0,-1),(0,1),(-1,0),(1,0)]
    height = len(grid)
    width = len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y] == startChar:
                start = (x,y)
 
    prev, goal = bfs(start)
    if not prev: return []                    # kein Pfad zum Ziel gefunden
    return reconstructPath(prev,goal)


f = open(r'C:\MyData\07_Kurse\PythonThemen\grids\maze1.txt')       
grid = f.read().splitlines()
f.close()

print(bfsPath(grid))