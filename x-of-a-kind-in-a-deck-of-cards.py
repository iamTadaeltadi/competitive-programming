class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2