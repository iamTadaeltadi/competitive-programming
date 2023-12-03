class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4500:
            return 1
        SERVING_OPTIONS = [(100, 0), (75, 25), (50, 50), (25, 75)]
        # (ml_soup_a, ml_soup_b) = [numerator, denominator]
        quantities_chance = {(n, n): [1, 1]}
        q = deque()
        q.appendleft((n, n))
        answer_numerator = 0
        answer_denominator = 1
        while q:
            ml_soup_a, ml_soup_b = q.pop()
            chance_numerator, chance_denominator = quantities_chance.pop((ml_soup_a, ml_soup_b))
            if min(ml_soup_a, ml_soup_b) <= 0:
                while answer_denominator < chance_denominator:
                    answer_numerator <<= 2
                    answer_denominator <<= 2
                if ml_soup_a <= 0:
                    answer_numerator += chance_numerator
                if ml_soup_b > 0:
                    answer_numerator += chance_numerator
                continue
            for serving_a, serving_b in SERVING_OPTIONS:
                remaining_soups = (ml_soup_a - serving_a, ml_soup_b - serving_b)
                if remaining_soups not in quantities_chance:
                    q.appendleft(remaining_soups)
                    quantities_chance[remaining_soups] = [0, chance_denominator << 2]
                quantities_chance[remaining_soups][0] += chance_numerator
        return answer_numerator / (answer_denominator << 1)
