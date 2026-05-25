class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        cur_sand = cur_stud = 0
        mismatches = 0
        while cur_sand < len(sandwiches) and mismatches < len(students) - cur_stud:
            if students[cur_stud] == sandwiches[cur_sand]:
                cur_sand += 1
                cur_stud += 1
                mismatches = 0
            else:
                students.append(students[cur_stud])
                cur_stud += 1
                mismatches += 1

        
        return len(sandwiches) - cur_sand