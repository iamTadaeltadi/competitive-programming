class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        x=[]
        xx=False
        for i in asteroids:
            while x and (abs(i)>abs(x[-1])) and ((i<0 and x[-1]>0)) :
                x.pop()
                
            if x and (abs(i)==abs(x[-1])) and ((i<0 and x[-1]>0)) :
                x.pop()
                continue
            if x and (abs(i)<abs(x[-1])) and ((i<0 and x[-1]>0)):
                pass
          
            else:x.append(i)
        return x
