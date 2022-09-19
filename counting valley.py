

def countingValleys(steps, path):
    c=[]
    v=0
    m=False
    valley=0
    for i in path:
        if i =="U" and "D" not in c:
            v+=1
        elif i =="U"  and "D" in c:
            c.pop()
        elif i=="D" and v!=0:
            v-=1
        elif i=="D" and v==0 :
            c.append(i)
            m=True
        if m and not c:
            valley+=1
            m=False
    return valley
