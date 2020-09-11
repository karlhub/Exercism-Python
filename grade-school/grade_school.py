class School:
    def __init__(self):
        self.school = dict()

    def add_student(self, name, grade):
        lst_grade = self.school.get(grade,[])
        lst_grade.append(name)
        self.school[grade] = lst_grade

    def roster(self):
        list_grades = [gr for gr in self.school.keys()]
        list_grades.sort()
        list_roster = []
        for gr in list_grades:
            list_gr = sorted(self.school.get(gr,[]))
            for st in list_gr:
                list_roster.append(st)
        return (list_roster)

    def grade(self, grade_number):
        return (sorted(self.school.get(grade_number,[])))

# Program tester
#sch = School()
#while True:
#    student = input ("Student: ")
#    if student == "done":
#        break
#    grade = input ("Grade: ")
#    sch.add_student(student, grade)
#    print ("School: ", sch.school)

#print ("Roster: ", sch.roster())

#while True:
#    grade = input ("Grade to search: ")
#    if grade == "done":
#        break
#    print ("Students: ", sch.grade(grade))

#print ("=> End of program")
