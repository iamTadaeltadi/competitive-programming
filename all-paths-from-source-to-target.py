class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        g=defaultdict(list)
        for node in range(len(graph)):
            for neg in graph[node]:
                g[node].append(neg)
        stack=[[0,[0]]]
        ans=[]
        while stack:
            curr,path=stack.pop()
            print(curr)
           
            if curr==len(graph)-1:
                ans.append(path)
            for neg in g[curr]:
                stack.append([neg,path+[neg]])
               
        return ans