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

    def scalar(self):
        if isinstance(self, (float, int)):
            assert all([isinstance(i, (float, int) ) for i in self]), 'The scalar only can be float or int'

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
        if isinstance(other, Mat) and self.shape() == other.shape():
            m = [[self.matrix[x][y] + other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))]
        return Mat(m)

    def __sub__(self, other):
        if isinstance(other, Mat) and self.shape() == other.shape():
            m = [[self.matrix[x][y] - other.matrix[x][y] for y in range (len(self.matrix[0]))] for x in range (len(self.matrix))]
        return Mat(m)
        
    # basically it's only multiply the number on the matrix a1*b1, a2*b2 etc
    def __mul__(self, other):
        return Mat([[(self.matrix[x][y] * other.matrix[x][y]) for y in range (len(other.matrix[0]))] for x in range (len(self.matrix))])

    def __truediv__(self, other):
        if isinstance(other, Mat) and self.shape() == other.shape():
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

    def scalar_operation(self, scalar):
        # addition
        add_result = [[elem + scalar for elem in row] for row in self.matrix]
        # substract
        sub_result = [[elem - scalar for elem in row] for row in self.matrix]
        # multiplication
        multi_result = [[elem * scalar for elem in row] for row in self.matrix]
        # division
        div_result = [[elem / scalar for elem in row] for row in self.matrix]

        # reverse opertion
        rev_add_result = [[scalar + elem for elem in row] for row in self.matrix]
        # reverse multi
        rev_multi_result = [[scalar + elem for elem in row] for row in self.matrix]

        return{
            'additon' : add_result,
            'subs' : sub_result,
            'multi' : multi_result,
            'divison' : div_result,
            'reverse_add' : rev_add_result,
            'reverse_mul' : rev_multi_result
        }

