class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        d=defaultdict(int)

        for i in bills:
            print(d)
            if i==10:
                if d[5]<1:
                    return False
                else:
                    d[5]-=1
            if i==20:
                if (d[10]<1 and d[5]<3)  or  d[5]<1:
                    return False
                else:
                    if d[10]>=1 and d[5]>=1:
                        d[10]-=1
                        d[5]-=1
                    elif d[5]>=3:
                        d[5]-=3
                    else:
                        pass


            d[i]+=1

        return True