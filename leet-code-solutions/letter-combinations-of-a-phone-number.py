class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ans=[]
        d=defaultdict(list)

        d["2"] = ["a","b","c"]
        d["3"] = ["d","e","f"]
        d["4"] = ["g","h","i"]
        d["5"] = ["j","k","l"]
        d["6"] = ["m","n","o"]
        d["7"] = ["p","q","r","s"]
        d["8"] = ["t","u","v"]
        d["9"] = ["w","x","y","z"]


        def backtrack(index,curr):
            print(curr)

            if len(digits)==len(curr):
                ans.append(curr)
                return 

            for i in range(index,len(digits)):
                for char in d[digits[index]]:
                    backtrack(i+1,curr+char)

        backtrack(0,"")

        if len(ans)==1 and ans[-1]=="":
            return ""
        return ans


            


