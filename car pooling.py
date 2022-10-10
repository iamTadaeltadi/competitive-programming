class Solution:
    def carPooling(self, trips, capacity):
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        print(lst)
        lst.sort()
        print(lst)
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
