class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        queue=deque()
        incoming=[0]*len(graph)

        for i in range(len(graph)):
            incoming[i] += len(graph[i])
            if  not graph[i] :
                queue.append(i)
            for child in graph[i]:
                g[child].append(i)
        
        safe=[]
        print(g)
        print(incoming)
        while queue:
            curr=queue.pop()
            safe.append(curr)
            
            for child in g[curr]:
                incoming[child]-=1
                if incoming[child]==0:
                    queue.append(child)
        
        safe.sort()
        return safe