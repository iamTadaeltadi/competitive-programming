class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=defaultdict(list)
        for row in range(len(isConnected)):
            for col in range(len(isConnected)):
                if isConnected[row][col]==1:
                    graph[row+1].append(col+1)
        visited=set()
        comp=0
        for node in graph:
            if node in visited:
                continue
            visited.add(node)
            stack=[node]
            while stack:
                curr=stack.pop()
                for neg in graph[curr]:
                    if neg not in visited:
                        visited.add(neg)
                        stack.append(neg)
            comp+=1
        return comp