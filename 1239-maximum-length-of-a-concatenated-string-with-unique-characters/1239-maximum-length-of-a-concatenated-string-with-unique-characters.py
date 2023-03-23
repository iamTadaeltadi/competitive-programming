class Solution:
    def maxLength(self, arr) -> int:
        def isUniqueChars(string):
            freq = Counter(string)
            if len(freq) == len(string):
                return True
            else:
                return False
        
        def cocatnate(index, curr):
            nonlocal res
            
            # Check if adding the current string results in unique characters
            if not isUniqueChars(curr + arr[index]):
                return
            
            # Update result if current concatenation has unique characters
            res = max(res, len(curr + arr[index]))
            
            # If all strings have been processed, return
            if index == len(arr) - 1:
                return
            
            # Recursively concatenate remaining strings
            for i in range(index + 1, len(arr)):
                cocatnate(i, curr + arr[index])
        
        res = 0
        for i in range(len(arr)):
            cocatnate(i, "")
        
        return res
            
            
        
