from sympy.ntheory import isprime

# calcolo prodotto tra 2 matrici

class Matrix:
    def __init__(self, mat):
        if len(mat) == 0: raise ValueError('Cannot create empty matrix')
        self.mat = mat
        self.rows = len(mat)
        self.cols = len(mat[0])
    def display(self):
        for i in range(self.rows):
            print(self.mat[i])
    
    

def sumvectors(v1, v2):
    return list(map(lambda x, y: x*y, v1, v2))

def matrix_product(m1, m2):
    m1 = Matrix(m1)
    m2 = Matrix(m2)
    print(m1.rows, m1.cols)
    
    if m1.cols == m2.rows:
        # 1, 2, 3       1, 2
        # 2, 3, 4   x   2, 3
        # 3, 4, 5       5, 6
        # 5, 6, 7
        # m x n -> n x k
        # m x k
        # 4x3, 3x2 ---->  4x2
        final_mat = []
        for i, row in enumerate(m1.mat):
            final_mat_row = []
            for j in range(m2.cols):
                colonna = [row[j] for row in m2.mat]
                item = sum(sumvectors(row, colonna))
                final_mat_row.append(item)
            final_mat.append(final_mat_row)
                
        return Matrix(final_mat)
        
    else:
        raise Exception('Cannot make the product of {}x{} matrix with {}x{} matrix'.format(m1.rows, m1.cols, m2.rows, m2.cols))
    
    
    
if __name__ == '__main__':
    pass