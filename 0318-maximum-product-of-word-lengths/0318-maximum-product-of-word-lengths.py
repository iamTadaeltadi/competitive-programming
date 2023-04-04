class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res=[]
        for word in words:
            x=0
            for char in word:
                x|=1<<ord(char)-97
            res.append(x)
        max_count=0
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                if res[i] &res[j]==0:
                    max_count=max(max_count,len(words[i])*len(words[j]))
        return max_count
                    