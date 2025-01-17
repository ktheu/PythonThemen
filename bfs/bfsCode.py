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
    '''
    returns:  Liste mit möglichen Folgestellungen zu state
    '''
    pass

def goaltest(state):
    '''
    returns: True, wenn state eine Lösung ist
    '''
    pass

def getMove(s1, s2):
    '''
    returns: die Beschreibung des Übergangs von state s1 zu state s2
    '''
    pass

  
#Aufruf:
#prev, goal = bfs(startstate)
#path = reconstructPath(prev,goal) 
#print(getMoves(path))