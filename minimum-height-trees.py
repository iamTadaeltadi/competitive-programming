class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph=defaultdict(list)
        queue=deque()
        ans=[]
        incoming=[0]*n

        for _from,_to in edges:
            graph[_from].append(_to)
            graph[_to].append(_from)
        
       
        for node in graph:
            #if node has only one negibors
            if len(graph[node])==1:
                queue.append([node,1])
            incoming[node]+=len(graph[node])

        while queue:
            curr,height=queue.popleft()
            ans.append([curr,height])
            for neg in graph[curr]:
                incoming[neg]-=1
                if incoming[neg]==1:
                    queue.append([neg,height+1])
        print(ans)
        res=[]
        if not ans:
            return [0]
        max_depth = max(item[1] for item in ans)
        for i in ans:
            if i[1]==max_depth:
                res.append(i[0])

        return res