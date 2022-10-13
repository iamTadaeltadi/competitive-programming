class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x=[[p,s] for p,s in zip(position,speed)]
        xx=[]
        for p,s in sorted(x):
            while xx and (xx[-1])<=(target-p)/s:
                xx.pop()
            xx.append((target-p)/s)
        return len(xx)
        
