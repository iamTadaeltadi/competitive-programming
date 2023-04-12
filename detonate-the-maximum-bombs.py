class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j:
                    h,k,r=bombs[i][0],bombs[i][1],bombs[i][2]
                    x,y=bombs[j][0],bombs[j][1]
                    
                    dis=math.sqrt((x-h)**2+(y-k)**2)
                    if dis<=r:
                        graph[i].append(j)
        count=1
        print(graph)
        for i in range(len(bombs)):
            stack=[i]
            visited=set()
            c=1
            while stack:
                curr=stack.pop()
                visited.add(curr)
                for neg in graph[curr]:
                    if neg not in visited:
                        stack.append(neg)
                        c+=1
            count=max(count,len(visited))
        return count