class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        ll=[]
        for i in range(len(left)):
            n=nums[left[i]:right[i]+1]
            m=max(n)
            mi=min(n)
            s=(m-mi)/(len(n)-1)
            if (m-mi)%(len(n)-1)!=0:
                ll.append(False)
                continue
            t=mi
            c=True
            for i in range(len(n)):
                if t in n:
                    t+=s
                else:
                    ll.append(False)
                    c=False
                    break
            if c:
                ll.append(True)
        return ll
                    
