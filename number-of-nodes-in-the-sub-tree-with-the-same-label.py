class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=defaultdict(list)
        res=[]
        for node,child in edges:
            graph[node].append(child)
            graph[child].append(node)
        ans=[0]*(n)
        visited=set()

        def dfs(node,visited):

            if node in visited:
                return [0]*26
            cnt=[0]*26
            visited.add(node)
            for neg in graph[node]:
                count=dfs(neg,visited)
                for i in range(26):
                    cnt[i]+=count[i]
            cnt[ord(labels[node])-97]+=1
            ans[node]+=cnt[ord(labels[node])-97]
            return cnt
        dfs(0,visited)
        return ans