import pandas as p, numpy as n, matplotlib.pyplot as m
p.DataFrame({'x': (x := n.linspace(0, 2*n.pi, 100)), 'Seno': n.sin(x), 'Coseno': n.cos(x)}).plot(x='x', style={'Seno': '-', 'Coseno': '--'})
m.show()
