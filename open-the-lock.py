class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        queue=deque()
        queue.append(("0000",0))

        visit = set(deadends)
        visit.add("0000")
        if target in deadends or "0000"  in deadends:
            return -1


        def children(lock):
            res = []

            for i in range(4):
                digit1 = (lock[:i]) + str((int(lock[i])+1)%10) +(lock[i+1:])
                digit2 = (lock[:i]) + str((int(lock[i])-1+10)%10) + (lock[i+1:])

                res.append(str(digit1))
                res.append(str(digit2))

            return res

        while queue:
            lock, path = queue.popleft()

            if lock==target:
                return path

            for neg in children(lock):
                if neg not in visit:
                    queue.append((neg,path+1))
                    visit.add(neg)

        return -1