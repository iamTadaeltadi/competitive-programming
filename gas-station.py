class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        amount, total, ans = 0, 0, 0
        for idx, (g, c) in enumerate(zip(gas, cost)):
            amount += g - c
            total += g - c
            if amount < 0:
                amount = 0
                ans = idx + 1
        return -1 if total < 0 else ans