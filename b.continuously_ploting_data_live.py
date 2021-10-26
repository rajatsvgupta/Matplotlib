import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):
    data=pd.read_csv("part9.csv")
    x=data["x_value"]
    y1=data["total_1"]
    y2=data["total_2"]
    plt.cla()
    plt.plot(x,y1,label="y1")
    plt.plot(x,y2,label="y2")
    print(x,y1,y2)
    plt.grid(True)
    plt.xlabel("Time in sec")
    plt.ylabel("Variation in Y value")
    plt.title("Variation of y values with time")
    plt.legend(loc="upper left")

a=FuncAnimation(plt.gcf(),animate,1000)
plt.tight_layout()
plt.show()
