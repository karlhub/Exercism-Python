class Garden:
    def __init__(self, diagram, students=[]):
        list_students = ["Alice","Bob","Charlie","David","Eve","Fred","Ginny","Harriet","Ileana","Joseph","Kincaid","Larry"]
#In Python 3.7.4 "new line" char inside a string is represented with just one '\', but in Python 3.8 it is needed 2 '\\'
        rows_windows = diagram.split("\n")
        if students == []:
            students = list_students
        students.sort()
        self.garden = [rows_windows, students]

    def plants (self, student):
        dict_plants = {"C":"Clover","G":"Grass","R":"Radishes","V":"Violets"}
        ind = self.garden[1].index(student)
        list_plants = [self.garden[0][0][ind*2],self.garden[0][0][ind*2+1],self.garden[0][1][ind*2],self.garden[0][1][ind*2+1]]
        list_plants_names = []
        for p in list_plants:
            list_plants_names.append(dict_plants.get(p))
        return (list_plants_names)

# Program tester
#list_diagram = "VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV"
#list_diagram = input ("Diagram: ")
#list_students = []
#while True:
#    student = input ("Student: ")
#    if student == "done":
#        break
#    list_students.append(student)
#print (list_students)
#grd = Garden(list_diagram, list_students)
#print ("Garden: ", grd.garden)

#while True:
#    student = input ("Student to search: ")
#    if student == "done":
#        break
#    print (grd.plants(student))

#print ("=> End of program")
