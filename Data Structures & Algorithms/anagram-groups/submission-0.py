class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = {}
        for i in strs:
            key = "".join(sorted(i))

            if key not in ls:
                ls[key] = []
            ls[key].append(i)

        return list(ls.values())
                
                