class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:



        answer = []
        self.graph = defaultdict(list)


        
        


        for i in range(len(equations)):
            self.graph[equations[i][0]].append([equations[i][1],values[i]])
            self.graph[equations[i][1]].append((equations[i][0],1/values[i]))
        # print(self.graph)

        for i in range(len(queries)):
            answer.append(self.dekstra(queries[i][0],queries[i][1]))
        return answer

    def dekstra(self,src,dst):
        seen = set()
        if src not in self.graph:
            return -1.00000
        heap = [(src,1)]

        while heap:
            node,weight = heap.pop()

            if node==dst:
                return weight

            seen.add(node)
            for i in self.graph[node]:
                print(weight)
                if i[0] not in seen:
                    
                    heap.append((i[0],i[1]*weight))
                    seen.add(i[0])
        return -1.00000

