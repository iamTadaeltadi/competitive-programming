class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi=0
        for i in range(len(trips)):
            maxi=max(max(trips[i]),maxi)
        path=[0]*(maxi+1)
        for i in trips:
            path[i[1]]+=i[0]
            path[i[2]]-=i[0]
        for i in range(1,len(path)):
            path[i]+=path[i-1]
        print(path)
        if max(path)>capacity:
            return False
        return True
            