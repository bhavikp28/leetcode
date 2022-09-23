class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            if s in students:
                while s != students[0]:
                    x = students[0]
                    students.pop(0)
                    students.append(x)
                students.pop(0)
            else:
                return(len(students))
        return 0