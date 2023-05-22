import tensorflow as tf
import numpy as np

# Tensor
tensor_1d = np.array([1.3, 1, 4.0, 23.99])
tensor_2d = np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)])
print('tensor 1d:', tensor_1d)
print('tensor 1d 0:', tensor_1d[0])
print('tensor 1d - 2:', tensor_1d[2])
print('tensor 2d:', tensor_2d)
print('tensor 2d - 3,2:', tensor_2d[3][2])

# Tensor Handling и Manipulations

matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype = 'int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')

print (matrix1)
print (matrix2)

matrix1 = tf.constant(matrix1)
matrix2 = tf.constant(matrix2)
matrix_product = tf.matmul(matrix1, matrix2)
matrix_sum = tf.add(matrix1,matrix2)
matrix_3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype = 'float32')
print ('matrix_3:', matrix_3)
