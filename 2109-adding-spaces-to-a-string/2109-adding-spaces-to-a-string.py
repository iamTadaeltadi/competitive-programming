class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        l=0
        st=[]
        for i in range(len(s)):
            if l<len(spaces) and i==spaces[l]:
                st.append(" ")
                st.append(s[i])
                l+=1
            else:
                st.append(s[i])
               
        return "".join(st)
                
        