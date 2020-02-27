class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        values = []
        for i,j in self.values: 
           row = []
           for k,l in zip(*other.values):
               row.append(i*k + j*l)
           values.append(row)
        return Matrix(values)

    def __rmatmul__(self, other):
        return self.__matmul__(other) 

    def __imatmul__(self, other):
        self.values = self.__matmul__(other).values
        return self