class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        changed.sort()
        original = []
        for num in changed:
            if counter[num] > 0:
                counter[num] -= 1
                if counter[2*num] > 0:
                    counter[2*num] -= 1
                    original.append(num)
                else:
                    return []
        return original

        
        
        
            
        
