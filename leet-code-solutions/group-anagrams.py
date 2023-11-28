class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        word_as_integer = defaultdict(list)

        for i in range(len(strs)):

            # x = strs[i].sort

            # print(sorted(strs[i]))

           
            
            word_as_integer["".join(sorted(strs[i]))].append(strs[i])

        ans = []


        for key in word_as_integer:
            ans.append(word_as_integer[key])
        return ans



