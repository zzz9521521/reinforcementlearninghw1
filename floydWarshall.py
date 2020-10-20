import numpy as np
import pandas as pd

inf = 99999999
e = np.zeros((10, 10), dtype = np.int)

n, m = map(int, input().split(''))

#initialize
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            e[i][j]=0
        else:
            e[i][j]=inf

#read line
for i in range(1, m+1):
    t1, t2, t3 = map(int, input().split(''))
    e[t1][t2] = t3

#Floyd-Warshall algorithm
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if e[i][j] > e[i][k] +e[k][j]:
                e[i][j] = e[i][k] + e[k][j]


for i in range(1, n+1):
    print(e[i][1:n+1])