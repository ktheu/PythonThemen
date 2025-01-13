
f = open(r'C:\MyData\07_Kurse\PythonThemen\grids\maze1.txt')       
grid = f.read().splitlines()
f.close()
height = len(grid)
width = len(grid[0])
for x in range(height):
    for y in range(width):
        if grid[x][y] == 'S':
            start = (x,y)
        elif grid[x][y] == 'Z':
            ziel = (x,y)

print(f'Höhe = {height}, Breite = {width}')
print(f'{start=}, {ziel=}')

dirs = [(0,-1),(0,1),(-1,0),(1,0)]    

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

def nextstates(state):
    '''
    returns:  Liste mit möglichen Folgestellungen zu state
    '''
    x, y = state
    tmp = []
    for xd, yd in dirs:
        x1 = x + xd
        y1 = y + yd
        if 0 <= x1 < height and 0 <= y1 < width and grid[x1][y1] != '#':
            tmp.append((x1,y1))
    return tmp    
    
def goaltest(state):
    '''
    returns: True, wenn state eine Lösung ist
    '''
    return state == ziel


# Aufruf:
prev, goal = bfs(start)
path = reconstructPath(prev,goal) 
print(path)