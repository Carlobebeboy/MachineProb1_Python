import matplotlib.pyplot as plot

from math import*

n = list(range(0,100))
x = []

def f():
    
    for i in range(0,100):
        y = (i**2)-7
        
        if i == 10:
            return 0
        
        elif i < 10:
            x.append(y)
            
        elif i > 100:
            
            break           
        else:
            b = b-10
            y = (b**2)-7
            x.append(y)
    
    return i
f()
v = x * 10
plot.stem(n, v, '-r', use_line_collection = True)