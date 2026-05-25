from collections import Counter, deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        idx = 0

        res = n
        for s in sandwiches:
            cnt = 0
            while cnt < n and students[idx] != s:
                idx += 1
                idx %= n
                cnt += 1
            
            if students[idx] == s:
                students[idx] = -1
                res -= 1
            else:
                break
        return res
