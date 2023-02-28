class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.x=x
        self.n=n
        
        result=self.pow(self.n)
        self.d={}
        return result
        
    def pow(self,n):
        if n==0:
            return 1
            if n<=1:
                return self.x
            if n%2==0:
                return (self.pow(n/2))**(2)
            else:
                return (self.pow(n//2))**(2) *self.x
        else:
            if n==-1 :
                return 1/self.x
            if n%2==0:
                return (self.pow(n/2))**(2)
            else:
                return (self.pow(n//2))**(2) *self.x

            
        