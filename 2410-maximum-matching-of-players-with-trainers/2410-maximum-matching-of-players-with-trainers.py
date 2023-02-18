class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        left=0
        n=len(players)
        m=len(trainers)
        right=0
        match_possible_no=0
        while left<n and right<m:
            if players[left] >trainers[right]: #this loop itterates for min of length of m or n
                right+=1 #push right cause no points in players point that are less than current right point
            else:
                match_possible_no+=1#counts match no 
                left+=1 #push both pointers cause we use them 
                right+=1
        return match_possible_no
                