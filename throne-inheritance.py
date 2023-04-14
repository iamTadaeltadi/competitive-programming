class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king=kingName
        self.graph=defaultdict(list)
        self.graph[kingName]=[]
        self.dead=set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].insert(0,childName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        if self.king==name:

            if len(self.graph[name])>=1:
                self.king==self.graph[name][-1]
            else:
                self.king=None

    def getInheritanceOrder(self) -> List[str]:
        if self.king:
            stack=[self.king]
            ans=[]
            while stack:
                curr=stack.pop()
                if curr not in self.dead:
                    ans.append(curr)
                for neg in self.graph[curr]:
                    stack.append(neg)
            return ans



        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()