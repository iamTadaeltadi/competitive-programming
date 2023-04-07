n=int(input())
from collections import defaultdict
matrix=[]

for row in range(n):
    rows=list(map(int,input().split()))
    matrix.append(rows)
tot=0
for row in range(n):
    for col in range(row,n):
        if matrix[row][col]:
            tot+=1
           



print(tot)
