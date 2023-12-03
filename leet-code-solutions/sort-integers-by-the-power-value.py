import math
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        answer = []
        def helper(num):

            if num == 1:
                return 1

            if num%2 == 0:
                return 1+helper(num/2)
            else:
                return helper(3*num +1) + 1




        for i in range(lo,hi+1):

            answer.append((helper(i),i))
        
        answer.sort()
        print(answer)
        return answer[k-1][1]


        
        