import numpy as np
from MatrixCluster import MatrixCluster

class MatrixManager():
    def __init__(self, array_x, array_z, filename):
        self.array_x = array_x
        self.array_z = array_z
        self.filename = filename
        self.array_y = self.get_matrix_from_file()
        self.is_inverse = self.get_is_inverse()
        
    def get_is_inverse(self):
        result = np.dot(self.array_x, self.array_z)
        return np.allclose(result, np.identity(3))
    
    def get_matrix_from_file(self):
        y=[]
        f = open(self.filename, 'r')     
        for line in f:                
            g=line.split(',')            
            y.append(g)
        self.array_y=np.array(y).astype(np.float16)
        print(self.array_y)

    def find_min_max_non_zero(self, test_array):
        masked_temp = np.ma.masked_equal(test_array, 0.0, copy=False)
        print(f"Minimum : {masked_temp.min()}, Maximum : {masked_temp.max()}")
        return masked_temp.min(), masked_temp.max()
    
    def write_to_file(self, value, filename):
        f =  open(filename, 'w')
        f.write(str(value))
        f.close()
        


x = np.array([[1, 1, 2.0], [3, 4, 5], [5, 4, 3]])
z=np.linalg.inv(x)
    

## Task 3.1
matrixmanager = MatrixManager(x,z, 'data.txt')
print("Z is inverse : ", matrixmanager.get_is_inverse())

## Task 3.2 
matrixmanager.get_matrix_from_file()

cluster = MatrixCluster(matrixmanager.array_y, 10, 10,10)

matrixmanager.find_min_max_non_zero(cluster.get_relative_distance())
cluster.get_com()
matrixmanager.write_to_file(cluster.get_com(), 'com.txt')