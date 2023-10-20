#Map to get pair mapping
    pairMap = defaultdict(int)
    #To get preference of person i with person j in O(1)
    prefer = {}
    
    #Populating pairMap
    for p1,p2 in pairs:
        pairMap[p1] = p2
        pairMap[p2] = p1
    
     #Populating prefer Map
    for i in range(len(preferences)):
        for j in range(n-1):
            if i not in prefer:
                prefer[i] = {}
            prefer[i][preferences[i][j]] = j
    
    #Looping through preferences again to find if person i is unhappy
    res = 0
    for i in range(len(preferences)):
        for j in range(n-1):
            x = i
            y = pairMap[x]
            u = preferences[x][j]
            v = pairMap[u]
            if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
                res+=1
                break
    return res