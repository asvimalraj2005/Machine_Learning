# Matrix multiplication in python 
# we can perform mathematical operations on any dimensions 1-D, 2-D, 3-D 
# add()        --> adds two matrix element wise 
# subtract()   --> subtracts two matrix element wise 
# divide()     --> divides two matrix element wise 
# multiply()   --> This function is used to perform element wise matrix multiplication
# dot()        --> This function is used to compute the matrix multiplication, rather than element wise multiplication 
# sqrt()       --> Returns the square root of the elements 
# sum(x,axis)  --> adds all the element in matrix , axis=0 the sum of column is provided , axis = 1 the sum of row is provided 
# "T"          --> This argument is used to transpose the specified matrix.  
#
# Below is the program for all the above operations
#
# import numpy
# a = numpy . array ( [ 1 , 2 ] ,
#                     [ 4 , 5 ] )
# b = numpy . array ( [ 7 , 8 ] ,
#                     [ 9 , 10] )
# print ( " Element wise sum " , numpy . add ( a , b ) ) 
# print ( " Element wise subtraction", numpy . subtract ( a , b ) )
# print ( " Element wise division " , numpy . divide ( a , b ) )
# print ( " Element wise multiplication " , numpy . multiply ( a , b ) )
# print ( " Element wise dot product " , numpy . dot ( a , b ) ) 
# print ( " Square root operation " , numpy . sqrt ( a ) ) 
# print ( " Summation of the matrices sum " , numpy . sum ( a ) )
# print ( " The column wise sum " , numpy . sum ( a , axis = 0 ) )
# print ( " The row wise sum " , numpy . sum ( a , axis = 1 ) ) 
# print ( " The transpose of given matrix is " , a . T )
# print ( " The modulus of the two matrices are " , numpy . mod ( a , b ) )
# print ( " The mean of the numerical python array " , a . mean ( a ) )
# print ( " The minimum element of the numerical array " , a . amin ( a ) )
# print ( " The maximum element of the numerical array " , a . amax ( a ) )


# There are lot of trignometric functions are also there used for other purposes 
# Matrix vectors , Determinants , Inverse of a matrix , Eigen values and Eigen vector ,=
