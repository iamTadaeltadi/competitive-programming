class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for i in dislikes:
            graph[i[0]].append(i[1])


        visit=set()
        for i in range(1,n+1):
            if i in visit:
                continue
            stack=[i]
            visit.add(i)
            a=set()
            a.add(i)
            b=set()
            turn=True
            while stack:
                curr=stack.pop()
                visit.add(curr)
                if curr in a:
                    turn=True
                if curr in b:
                    turn=False

                for neg in graph[curr]:
                    if turn:
                        if neg in a:
                            return False
                        b.add(neg)
                    else:
                        if neg in b:
                            return False
                        a.add(neg)
                    if neg not in visit:
                        stack.append(neg)
                

        return True