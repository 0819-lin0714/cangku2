# -*- coding: utf-8 -*-
#2.10.1
import numpy as np  
mat1 = np.mat("1 2 3; 4 5 6; 7 8 9") 
mat2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr1 = np.eye(3)
arr2 = 3*arr1
mat = np.bmat("arr1 arr2; arr1 arr2")

#2.10.2
import numpy as np
mat = np.matrix(np.arange(4).reshape(2, 2))
mT=mat.T
mH=mat.H
mI=mat.I

mat1 = np.mat("1 2 3; 4 5 6; 7 8 9")
mat2 = mat1*3
mat3=mat1+mat2
mat4=mat1-mat2
mat5=mat1*mat2
mat6=np.multiply(mat1, mat2) #点乘

#2.10.3
mat = np.mat('1 1 1; 1 2 3; 1 3 6')
inverse = np.linalg.inv(mat)
A=np.dot(mat, inverse)

A = np.mat("1,-1,1; 2,1,0; 2,1,-1")
b = np.array([4, 3, -1])
x = np.linalg.solve(A, b)#线性方程组Ax=b的解

A = np.matrix([[1, 0, 2], [0, 3, 0], [2, 0, 1]])
#A_value= np.linalg.eigvals(A)
A_value, A_vector = np.linalg.eig(A)

A = np.mat("4.0,11.0,14.0;  8.0,7.0,-2.0")
U, Sigma, V = np.linalg.svd(A, full_matrices=False)

A = np.mat("3,4; 5,6")
A_value=np.linalg.det(A)

