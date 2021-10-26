import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
index=count()
x=[]
y=[]

def animate(i):
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y,label="y")
    plt.grid(True)
    plt.xlabel("Time in sec")
    plt.ylabel("Variation in Y value")
    plt.title("Variation of y value with time")
    plt.legend(loc="upper left")

a=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.tight_layout()
plt.show()
