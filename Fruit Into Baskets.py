class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_picked = 0
        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_picked = max(max_picked, right - left + 1)
        return max_picked
