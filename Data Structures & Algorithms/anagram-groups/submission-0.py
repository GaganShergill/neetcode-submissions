from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in mydict:
                mydict[sorted_s].append(s)
            else:
                mydict[sorted_s] = [s]

        res = []
        for a in mydict.values():
            res.append(a)
        
        return res
