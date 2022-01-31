import pandas as pd
import numpy as np
import copy
class MatrixConvolver:
    """
    the constractor it set a new and empty list
    """
    def __init__(self):
        self.matrices_list =[]
    def add_matrix(self,matrix):
        if len(self.matrices_list) == 0:
            self.matrices_list.append(matrix)
        elif self.matrices_list[0].shape == matrix.shape:
            self.matrices_list.append(matrix)
    """
    if ​element ​ is a ndarray, remove the first matrix in matrices_list ​ that is equal to ​element ​ . If ​element ​ is of type int, remove matrix at index element ​ from ​matrices_list ​ . Otherwise, return -1.
    """
    def remove_matrix(self, element):
        if type(element) == int:
            del self.matrices_list[element]
        elif type(element) == np.ndarray:
            for i in range(len(self.matrices_list)):
                if np.array_equal(self.matrices_list[i],element):
                    del self.matrices_list[i]
                    break
        else:
            return -1
    """
    Reshape all matrices in ​matrices_list ​ to the shape new_shape ​ which is a tuple of integers.​ ​ If ​matrices_list ​ is empty, return 0. If matrices_list is not empty, try to reshape the matrices and replace each matrix in matrices_list with it’s reshaped version. If an exception occurs, return -1
    """
    def reshape_matrices(self,new_shape):
        try:
            if len(self.matrices_list) == 0:
                return 0
            else:
                for i in range(len(self.matrices_list)):
                    self.matrices_list[i]=np.reshape(self.matrices_list[i], new_shape)
        except:
            return -1
    """
    return a copy of the list
    """
    def get_matrices(self):
        return copy.deepcopy(self.matrices_list)
    """
    Return the output after performing a convolution operation with ​filter_matrix ​ with a stride of size ​stride_size ​ , over matrix at index ​i ​ in the matrices_list ​ attribut
    """
    def conv(self, i, filter_matrix, stride_size=1):
        m, n = filter_matrix.shape
        if m==n:
            y, x = self.matrices_list[i].shape
            y = ((y-m)//stride_size) + 1
            x = ((x-n)//stride_size) + 1
            new_image = np.zeros((y,x))
            for j in range(0,y,stride_size):
                for z in range(0,x,stride_size):
                    new_image[j][z] = np.sum(self.matrices_list[i][j:j+m, z:z+m]*filter_matrix)
            return new_image