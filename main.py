from numpy import *

arr = array([[1, 2, 3],[4, 5, 6]])
m1 = matrix([[1, 2, 3],
             [4, 5, 6]])
m2 = matrix('1 2;'
            ' 3 4;'
            ' 5 6')
print(m1 * m2)