class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            freq[k].append(s)
        

        return list(freq.values())
