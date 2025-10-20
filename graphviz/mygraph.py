from graphviz import Digraph

G = {'a': set('bc'),
     'b': set('d'),
     'c': set('ed'),
     'd': set('g'),
     'e': set(),
     'f': set('d'),
     'g': set('e')}  

dot = Digraph(engine="neato", format='png')   # neato = positionsbasiertes Layout
# dot.attr(splines="false", overlap="false")

dot.node("e", pos="2,0!")
for u, neighbors in G.items():
    for v in neighbors:
        dot.edge(u, v)

dot.render('mygraph',view=True)