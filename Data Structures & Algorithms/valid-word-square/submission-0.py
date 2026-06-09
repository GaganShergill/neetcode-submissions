class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        words_col = []
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))

        for i in range(max_len):
            tmp_str = []
            j = 0
            while j < len(words) and i < len(words[j]):
                tmp_str.append(words[j][i])
                j += 1
            words_col.append("".join(tmp_str))
        
        for i, word in enumerate(words):
            if word != words_col[i]:
                return False
        
        return True
