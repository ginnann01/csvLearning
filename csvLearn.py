import csv
import numpy as np

def getData(N, A, B):
    x = np.array(range(0,N), dtype=np.float32)/N*4*np.pi
    y = np.sin(x*B)*A
    return x, y


[x, y1] = getData(100, 1, 1)
[x, y2] = getData(100, 2, 2)
[x, y3] = getData(100, 1, 3)

with open("sin.csv", 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for r in zip(x, y1, y2, y3):
        writer.writerow(r)