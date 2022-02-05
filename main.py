from numpy import *

# arr = array([[2, 0, -1],[4, 5, 6]])
m1 = array([[2, 0, -1],
             [5, 1, 0],
             [0, 1, 3]])
print(type(m1))
m1 = matrix(m1)
print(type(m1))
m2 = matrix([[3, -1, 1],
             [-15, 6, -5],
             [5, -2, 2]])
m3 = matrix('3 -1 1; -15 6 -5; 5 -2 2')
print(m3)
print(type(m2))
print(m1 * m2)
print(m2 * m1)