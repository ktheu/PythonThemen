
def nb(pos):
    '''
    pos: Tuple (x,y) - die Position im grid
    returns: Liste mit den möglichen Nachbarpositionen
    '''
    x, y = pos
    tmp = []
    for xd, yd in dirs:
        x1 = x + xd
        y1 = y + yd
        if 0 <= x1 < height and 0 <= y1 < width and grid[x1][y1] != '#':
            tmp.append((x1,y1))
    return tmp    

from collections import deque
def bfs(startstate):
    ''' 
    returns: Tupel (prev, state) 
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

def nextstates(state):
    '''
    state: Spielstellung
    returns:  Liste mit möglichen Folgestellungen zu state
    '''
    return nb(state)

def goaltest(state):
    '''
    state: Spielstellung
    returns: True, wenn state eine Lösung ist
    '''
    return state ==  ziel

def getMove(s1, s2):
    '''
    (optional)
    returns: die Beschreibung des Übergangs von state s1 zu state s2
    '''
    x1,y1 = s1
    x2,y2 = s2
    if x1 < x2: return 'D'   # down
    if x1 > x2: return 'U'   # up
    if y1 < y2: return 'R'   # right
    if y1 > y2: return 'L'   # left

def getMoves(path):
    '''
    (optional)
    returns: Beschreibung des Pfads
    '''
    weg = ''
    for i in range(len(path)-1):
        weg+=getMove(path[i],path[i+1])
    return weg


f = open(r'C:\MyData\07_Kurse\PythonThemen\grids\maze2.txt')       
grid = f.read().splitlines()
f.close()

# Höhe und Breite des Labyrinths
height = len(grid)
width = len(grid[0])
print(f'Höhe = {height}, Breite = {width}')

# Bewegungsrichtungen
dirs = [(0,-1),(0,1),(-1,0),(1,0)]    

# Start- und Zielposition finden
for x in range(height):
    for y in range(width):
        if grid[x][y] == 'S':
            start = (x,y)
        elif grid[x][y] == 'Z':
            ziel = (x,y)
print(f'{start=}, {ziel=}')

prev, goal = bfs(start)
path = reconstructPath(prev,goal)
print(path)
print(getMoves(path))