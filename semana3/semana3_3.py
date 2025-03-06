import pandas as p
import numpy as n
import matplotlib.pyplot as m

x = n.linspace(0, 6.28, 100)
grafica_plot = p.DataFrame({'x': x, 
                            'Seno': n.sin(x), 
                            'Coseno': n.cos(x)})

grafica_plot.plot(x='x')
m.show()

