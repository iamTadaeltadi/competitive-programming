class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sett=Counter(words[0])
        for i in range(1,len(words)):
            for j in sett:
                if (j in Counter(words[i])) and sett[j]==Counter(words[i])[j]:
                    pass
                elif (j in Counter(words[i])):
                    sett[j]=min(Counter(words[i])[j],sett[j])
                else:
                    sett[j]=0
        print(sett)
        listt=[]
        for i in sett:
            if sett[i]!=0:
                listt.append(i*sett[i])
        return "".join(listt)
                

                
                
                    
            
        