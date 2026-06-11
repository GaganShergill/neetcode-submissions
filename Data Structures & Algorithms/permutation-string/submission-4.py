class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_counts = Counter(s1)
        window_counts = Counter()
        matches = 0
        
        for i in range(n2):
            window_counts[s2[i]] += 1
            if s2[i] in s1_counts and window_counts[s2[i]] == s1_counts[s2[i]]:
                matches += 1

            if i >= n1:
                left_char = s2[i - n1]
                if left_char in s1_counts and window_counts[left_char] == s1_counts[left_char]:
                    matches -= 1

                if window_counts[left_char] == 1:
                    del window_counts[left_char]
                else:
                    window_counts[left_char] -= 1


            if matches == len(s1_counts):
                return True
        
        return False

