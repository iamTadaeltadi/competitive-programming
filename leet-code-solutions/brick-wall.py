class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        dic = defaultdict(int)
        

        for row in range(len(wall)):
            prefix = 0
            for col in range(len(wall[row])):
                prefix+= wall[row][col]
                dic[prefix]+=1

        
        del dic[prefix]
        
        

        return len(wall)- (max(dic.values()) if dic  else 0)
                