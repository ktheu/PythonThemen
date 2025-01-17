'''
Solve a Maze with BFS
'''

from collections import deque
def bfs(startstate):
    ''' 
    returns: Tuple (prev, state) 
        prev: dictionary mit den Vorgängern der untersuchten Spielstellungen,            
        state: Spielstellung, die den goaltest besteht
        wenn Ziel nicht gefunden: None, None
    '''   
    frontier =  deque([startstate])
    prev = {startstate:None}
    while frontier:
        state = frontier.popleft()  
        if goaltest(state):
            return prev, state
        for v in nextstates(state):
            if v not in prev:
                frontier.append(v)
                prev[v] = state
    return None, None

def reconstructPath(prev,goalstate):
    state = goalstate
    path = []
    while state is not None:
        path.append(state)
        state = prev[state]
    path.reverse()
    return path

def getMoves(path):
    '''
    returns: Beschreibung des Pfads als eine Folge von Aktionen (Moves)
    '''
    moves = ''
    for i in range(len(path)-1):
        moves+=getMove(path[i],path[i+1])
    return moves

def nextstates(state):
    x, y = state
    tmp = []
    for xd, yd in dirs:
        x1 = x + xd
        y1 = y + yd
        if 0 <= x1 < height and 0 <= y1 < width and grid[x1][y1] != '#':
            tmp.append((x1,y1))
    return tmp  

def goaltest(state):
    return state == ziel

def getMove(s1, s2):
    x1,y1 = s1
    x2,y2 = s2
    if x1 < x2: return 'D'   # down
    if x1 > x2: return 'U'   # up
    if y1 < y2: return 'R'   # right
    if y1 > y2: return 'L'   # left
    
def showGridCoordinates(grid):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                print('  #  ', end=' ')
            elif grid[i][j] == 'S':
                print('  S  ', end=' ')
            elif grid[i][j] == 'Z':
                print('  Z  ', end=' ')
            else:
                print(f'({i},{j})', end=' ')
        print()
    print()
  
f = open(r'C:\MyData\07_Kurse\PythonThemen\bfs\maze1.txt')       
grid = f.read().splitlines()
f.close()

# Höhe und Breite des Labyrinths
height = len(grid)
width = len(grid[0])
dirs =  [(0,-1),(0,1),(-1,0),(1,0)]    

print(f'Höhe = {height}, Breite = {width}')

# Start- und Zielposition finden
for x in range(height):
    for y in range(width):
        if grid[x][y] == 'S':
            start = (x,y)
        elif grid[x][y] == 'Z':
            ziel = (x,y)
print(f'{start=}, {ziel=}')

showGridCoordinates(grid)

# prev, goal = bfs(start)
# path = reconstructPath(prev,goal)
# print(path)
# print(getMoves(path))