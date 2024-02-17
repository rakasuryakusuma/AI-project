class Mat:
    def __init__(self, matrix):
        if isinstance(matrix[0], list):
            col_length = len(matrix[0])
            for i, row in enumerate(matrix):
                assert all([isinstance(r, (float, int)) for r in row]), "Mat can only be 2D matrix"
                
            self.matrix = matrix

        elif isinstance(matrix[0], (float, int)):
            # for i, row in enumerate(matrix):
            assert all([isinstance(r, (float, int)) for r in row]), "The matrix only can contain float or int"
            self.matrix = [matrix]
        self.shape = self._shape()
        self.str = self.__str__()

        # self.shape = self.shape()
    def __str__(self):
        '''
        Special function to handle print
        '''
        def max_list(lst):
            'takes an arbitrarily nested list as a parameter and returns the maximum element the sub-list has.'
            if isinstance(lst[0], list):
                return max([max_list(x) for x in lst])
            else:
                return max([round(l,2) for l in lst])
        max_len = len(str(max_list(self.matrix))) + 4

        pretty_print = ""

        for row in self.matrix:
            if not (isinstance(row, list)):
                pretty_print += str(f"{row:.2f}") + " "
            else:
                pretty_print += "  "
                for col in row:
                    pretty_print += str(f"{col:.2f}").ljust(max_len) + " "
                pretty_print += "\n"
        
        if not (isinstance(row, list)):
            pretty_print = "Matrix(\n  "+pretty_print+"\n)"
        else:
            pretty_print = "Matrix(\n"+pretty_print+")"

        return pretty_print     
    
    def _shape(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return [rows, cols]

    def transpose(self):
        trans_mat = [[self.matrix[x][y] for x in range (len(self.matrix))] for y in range (len(self.matrix[0]))]
        return Mat(trans_mat)

    def __add__(self, other):
        if isinstance(other, Mat) and self.shape == other.shape:
            m = [[self.matrix[x][y] + other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))]
        return Mat([[self.matrix[x][y] + other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))])

    def __sub__(self, other):
        if isinstance(other, Mat) and self.shape == other.shape:
            m = [[self.matrix[x][y] - other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))]
        return Mat(m)
        
    # basically it's only multiply the number on the matrix a1*b1, a2*b2 etc
    def __mul__(self, other):
        return Mat([[(self.matrix[x][y] * other.matrix[x][y]) for y in range (len(other.matrix[0]))] for x in range (len(self.matrix))])

    def __truediv__(self, other):
        if isinstance(other, Mat) and self.shape == other.shape:
            # m = [[self.matrix[x][y] / other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))]
            return Mat([[self.matrix[x][y] / other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))])
        
    def __floordiv__(self, other):
        return Mat([[self.matrix[x][y] // other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))])
    
    def __matmul__(self, other):
        return [[sum(self.matrix[x][z] * other.matrix[z][y] for z in range (len(other.matrix))) for y in range (len(other.matrix[0]))] for x in range (len(self.matrix))]
    
    # to create one line matrix instead of 2d matrix
    def flatten(self):
        fm = [e for row in self.matrix for e in (row if isinstance (row, list) else [row])]
        self.matrix = [fm]

    def add(self):
        m = [[i + 2 for i in row] for row in self.matrix]
        return Mat(m)
    
    def __radd__(self):
        rm = [[2 + i for i in row] for row in self.matrix]
        return Mat(rm)
    
    def addMMZ(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrix must have the same shape to do this addition")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        elif isinstance(other, MatZeros):
            raise TypeError("Unsupported type for addition: Mat and MatZeros")
        else:
            raise TypeError("Unsupported type for addition")
        
    def addMMO(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrix must have the same shape to do this addition")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        elif isinstance(other, MatOnes):
            raise TypeError("Unsupported type for addition: Mat and MatOnes")
        else:
            raise TypeError("Unsupported type for addition")
        
    def addMMR(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrix must have the same shape to do this addition")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        elif isinstance(other, MatRandom):
            raise TypeError("Unsupported type for addition: Mat and MatRandom")
        else:
            raise TypeError("Unsupported type for addition")
        
    def determinant(self):
        # if self.shape != self.shape[0]:
        #     raise ValueError("Matrix must be a square")
        # determinant of a 2x2 matrix
        if self.shape == (2,2):
            a, b = self.matrix[0]
            c, d = self.matrix[1]
            return a * d - b * c
        # determinant of 3x3 matrix
        elif self.shape == (3, 3):
            a, b, c = self.matrix[0]
            d, e, f = self.matrix[1]
            g, h, i = self.matrix[2]
            return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
        else:
            raise ValueError("Determinant calculation is only for 2x2 and 3x3 matrix")
        
    def inverse(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("Matrix must be square for inversion.")
        
        if self.shape == (3, 3):
            det_A = self.determinant()
            if det_A == 0:
                raise ValueError("Matrix is singular, and the inverse does not exist.")
            
            a, b, c = self.matrix[0]
            d, e, f = self.matrix[1]
            g, h, i = self.matrix[2]

            # Calculate the adjugate matrix
            adjugate_A = Mat([
                [e*i - f*h, c*h - b*i, b*f - c*e],
                [f*g - d*i, a*i - c*g, c*d - a*f],
                [d*h - e*g, b*g - a*h, a*e - b*d]
            ])

            # Calculate the inverse matrix
            inv_A = adjugate_A.scalar_multiply(1/det_A)

            return inv_A
        else:
            raise ValueError("Inverse calculation is currently supported only for 3x3 matrices.")


# Creating three new object that inherits from Matrix object ( MatZeros, MatOnes, MatRandom)
class MatZeros(Mat):
    def __init__(self, matrix):
        super().__init__(matrix)

    def add(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrices must have the same shape for element-wise addition.")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        else:
            raise TypeError("Unsupported type for addition: MatZeros and {}".format(type(other).__name__))      
        
class MatOnes(Mat):
    def __init__(self, matrix):
        super().__init__(matrix)

    def add(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrices must have the same shape for element-wise addition.")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        else:
            raise TypeError("Unsupported type for addition: MatZeros and {}".format(type(other).__name__))
                
class MatRandom(Mat):
    def __init__(self, matrix):
        super().__init__(matrix)

    def add(self, other):
        if isinstance(other, Mat):
            if self.shape != other.shape:
                raise ValueError("Matrices must have the same shape for element-wise addition.")
            
            m = [[a + b for a, b in zip(row_self, row_other)] for row_self, row_other in zip(self.matrix, other.matrix)]
            return Mat(m)
        else:
            raise TypeError("Unsupported type for addition: MatZeros and {}".format(type(other).__name__))        

    # def scalar_operation(self):
    #     # addition
    #     add_result = [[elem + 2 for elem in row] for row in self.matrix]
    #     # substract
    #     sub_result = [[elem - 2 for elem in row] for row in self.matrix]
    #     # multiplication
    #     multi_result = [[elem * 2 for elem in row] for row in self.matrix]
    #     # division
    #     div_result = [[elem / 2 for elem in row] for row in self.matrix]

    #     # reverse opertion
    #     rev_add_result = [[2 + elem for elem in row] for row in self.matrix]
    #     # reverse multi
    #     rev_multi_result = [[2 + elem for elem in row] for row in self.matrix]

    #     return{
    #         'additon' : add_result,
    #         'subs' : sub_result,
    #         'multi' : multi_result,
    #         'divison' : div_result,
    #         'reverse_add' : rev_add_result,
    #         'reverse_mul' : rev_multi_result,
            
    #     }

