class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list=[]
        for i in range(0,n):
            if (i+1)%3==0 and (i+1)%5==0 :
                list.append( "FizzBuzz")
            elif (i+1)%3==0:
                list.append("Fizz")
            elif (i+1)%5==0:
                 list.append("Buzz")
            else:list.append(str(i+1))
        return list
        
