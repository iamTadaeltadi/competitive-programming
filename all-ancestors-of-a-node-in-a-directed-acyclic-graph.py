class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        queue=deque()
        seen=set()
        incoming=[0]*n
        ancestor= [set() for _ in range(n)]
        res=[[] for i in range(n)]
        graph=defaultdict(list)
    
    

        for a,b in edges:
            graph[a].append(b)
            incoming[b]+=1


        for i in range(len(incoming)):
            if not incoming[i]:
                queue.append(i)
       
        while queue:

            curr=queue.pop()

            for neg in graph[curr]:
                incoming[neg]-=1
                
                for i in ancestor[curr]:
                    ancestor[neg].add(i)

                ancestor[neg].add(curr)

                if incoming[neg]==0:
                    queue.append(neg)

        for i in range(len(res)):

            res[i]=sorted(ancestor[i])
        
        return res