class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        priority = {}
		#making priority dictonary
        for p1, p2 in pairs:
            priority[p1] = preferences[p1][:preferences[p1].index(p2)]
            priority[p2] = preferences[p2][:preferences[p2].index(p1)]
        #start the iteration
        res = 0 #act as a counter for unhappy friends
        for p1 in priority:
            for p2 in priority[p1]:
                if p1 in priority[p2]:
                    res += 1
                    break
        return res