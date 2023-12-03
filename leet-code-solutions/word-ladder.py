class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue=deque([[beginWord,0]])
        seen=set()
        seen.add(beginWord)


        while queue:
            curr,path=queue.popleft()
           
            if curr==endWord:
                return path +1
            
            for word in wordList:
                diff=0
                if word not in seen:
                
                    for i in range(len(curr)):
                        if curr[i]!=word[i]:
                            diff+=1
                        if diff>=2:
                            break
                    
                    if diff==1:
                            queue.append([word,path+1])
                            seen.add(word)
        return 0




