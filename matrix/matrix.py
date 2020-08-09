class Matrix:
#In Python 3.7.4 "new line" char inside a string is represented with just one '\', but in Python 3.8 it is needed 2 '\\'
    def __init__(self, matrix_string):
        self.matrix = [[int(c) for c in r.split()] for r in matrix_string.split('\\n')]

    def row(self, index):
        return (self.matrix[index-1])

    def column(self, index):
        return ([r[index-1] for r in self.matrix])

# Program tester
#matStr = input ("Input Matrix String: ")
#matr = Matrix(matStr)
#print ("Matrix: ", matr.matrix)

#rowMatr = int (input ("Row: "))
#print (matr.row (rowMatr))

#colMatr = int (input ("Column: "))
#print (matr.column (colMatr))

#print ("=> End of program")
