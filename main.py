from numpy import *

arr = array([[2, 0, -1, 1, 2, 3],
             [4, 5, 6, 32, -5, 0]])
print(arr)
print("Data type : ", arr.dtype)
print("Dimension : ", arr.ndim)
print("Order of Array :", arr.shape)
print("Length of entire block :", arr.size)

print("\nThe method flatten() flattens any array and makes 1D array")
arr2 = arr.flatten()
print(arr2)

print("\nThe method reshape() is reverse of flatten()")
arr3 = arr2.reshape(3, 4)
print(arr3)

print("-----------------------------------------------------\n")
print("\nAll operations that can be applied on array can also be applied on matrix")
a = array([[2, 0, -1],
           [5, 1, 0],
           [0, 1, 3]])
print(type(a))
print("The function numpy.matrix() converts an array into a matrix")
m = matrix(a)
m1 = matrix('3 -1 1; -15 6 -5; 5 -2 2')
m2 = matrix([[3, -1, 1],
             [-15, 6, -5],
             [5, -2, 2]])
print(m)
print(type(m))
print(m1)
print("Diagonal of matrix m : ", diagonal(m))
print(m1.min())
print("Matrix operations")
print(m1 + m2)
print(m1 * m2)
