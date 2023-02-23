class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cur=defaultdict(int)
        t_count=Counter(t)
        m=float('inf')
        l=0
        def compare(t_count,cur):
            if len(cur) ==len(t_count):
                for i in t_count:
                    if i in cur:
                        if cur[i]<t_count[i]:
                            return False
                return True
            return False
        left, right = -1, -1
        for r in range(len(s)):
            if s[r] in t_count:
                cur[s[r]]+=1
            x=compare(t_count,cur)
            while len(cur) ==len(t_count) and compare(t_count,cur):
                if left == -1 or r-l+1 < m:
                    left, right = l, r
                m=min(r-l+1,m)
                if s[l] in cur:
                    cur[s[l]]-=1
                    if cur[s[l]]==0:
                        del cur[s[l]]
                
        
                l+=1
            
        if left == -1:
            return ""
        
        return (s[left:right+1])
                    
                    
                
                
            
            
        