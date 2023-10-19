class Union:
    def __init__(self,size):
        self.size = size
        self.parent = [i for i in range(size)]

    def find(self,member):
        print(member,"find")
        member ,root= ord(member)-97, ord(member)-97

        while root !=self.parent[root]:
            root =self.parent[root]
        
        while member !=root:
            parent = self.parent[member]
            self.parent[member]=root
            member = parent
        return root
    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)

        if  repx != repy:

            if repx <repy :
                self.parent[repy] = repx
            elif repy <repx:
                self.parent[repx] = repy
            else:
                self.parent[repy] = repx
                


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        uni = Union(26)

        for i in range(len(s1)):
            uni.union(s1[i],s2[i])


        answer = []
        

        for i in baseStr:
            print(i,"asa")
            answer.append(chr(uni.find(i)+97))

        return  "".join(answer)