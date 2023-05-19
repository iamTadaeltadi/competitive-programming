class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        queue=deque()
        ans=[[],[]]
        level=0
        n = len(adjacentPairs) + 1
        incoming = defaultdict(int)

        for i,j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
            incoming[i-1]+=1
            incoming[j-1]+=1
        
        for i,v in incoming.items():
            if v==1:
                queue.append([i+1,level])
                level+=1
            
        while queue:
            curr,le=queue.pop()
            ans[le].append(curr)

            for adj in graph[curr]:
                incoming[adj-1]-=1

                if incoming[adj-1]==1:
                    queue.append([adj,le])
                    
        result=ans[0]+ ans[1][::-1]
        
        return result










