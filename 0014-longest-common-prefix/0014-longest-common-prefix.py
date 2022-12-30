class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        maxx=strs[0]
        for i in strs:
            if len(i) <len(maxx):
                maxx=i
        se={}
        c=0
        maa=maxx
        ma=""
        for i in range(len(strs)):
            c=0
            ma=''
            while c<len(maxx) and maxx[c]==strs[i][c]:
                if len(ma)<len(maa):
                    ma=maxx[:c+1]
                c+=1
                
            maa=ma
            
        return ma
                
                

        