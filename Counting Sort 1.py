def countingSort(arr):
    # Write your code here
    x=[0]*100
    d={v:0 for v in arr}
    for j in arr:
        d[j]+=1
    for v,c in d.items():
        x[v]=c
    return x
