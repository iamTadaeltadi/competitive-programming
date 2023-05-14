class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:


        graph=defaultdict(list)
        d={}
        queue=deque()
        outgoing=[0]*len(quiet)
        for  a,b in richer:
            graph[a].append(b)
            outgoing[b]+=1
        


   
        for i,v in enumerate(outgoing):
            if not v:
                queue.append([i,i])
        ans=[0]*len(quiet)
        # print(queue)
        # print(graph)
        # print(outgoing)
        for i in range(len(quiet)):
            d[i]=i
        
        while queue:
            curr,leastQuiet=queue.popleft()
            
            ans[curr]=leastQuiet
            print(curr,leastQuiet)

            for neg in graph[curr]:
                
                if quiet[leastQuiet]<quiet[d[neg]]:
                    d[neg]=leastQuiet
                     
                
                outgoing[neg]-=1
                if outgoing[neg]==0:
                    queue.append([neg,d[neg]])
                    
                   

        return ans