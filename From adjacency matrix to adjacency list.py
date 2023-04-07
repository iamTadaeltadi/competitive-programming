n=int(input())
from collections import defaultdict
matrix=[]
graph=defaultdict(list)
for row in range(n):
    rows=list(map(int,input().split(" ")))
    for col in range(n):
        if rows[col]==1:
            graph[row+1].append(col+1)

for vertex in range(1,n+1):
    print(len(graph[vertex]),*graph[vertex])
