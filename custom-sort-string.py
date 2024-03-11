class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)

        ans = []
        x = set()

        for i in order:
            if i in count:
                ans.append(i*count[i])
                x.add(i)
        for i in s:
            if i not in x:
                ans.append(i*count[i])
                x.add(i)
        return "".join(ans)