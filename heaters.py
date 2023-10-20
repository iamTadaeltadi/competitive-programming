class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        c,m=0,0
        for i in range(len(houses)):
           
            while c<len(heaters)-1 and abs(houses[i]-heaters[c])>=abs(houses[i]-heaters[c+1]):
                c+=1
            m=max(m,abs(houses[i]-heaters[c]))
        return m