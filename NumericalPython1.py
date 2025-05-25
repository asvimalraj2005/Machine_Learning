# Introduction about Numpy Python or Numerical Python 
# Numpy is a python library used for working with arrays 
# It is used to work with in the domain of linear algebra, fourier transform, and matrices 
# Normal arrays always slow for processing while on the other hand the numpy(numerical python) provides a way for faster efficient processing of data 
# Because numpy array stores the element in continuous location not alike list which stores the element in different location 
# To install numpy just use --> pip install numpy 
# 
#
# To import that downloaded library from the internet on your python file just add this line 
# import numpy 
# arr = numpy. array ( [ 1 , 2 , 3 , 4 , 5 ] )
# print ( arr )
#
#
# Numpy library can be imported as the alias with the as keyword while importing 
#
# import numpy as np 
# arr = np . array ( [ 1 , 2 , 3 , 4 , 5 ] )
# print ( arr )
#
#
# How to check what version of numpy library we are using 
#
# 
# import numpy as np
# print(np.__version__)
#
#
# import numpy as np 
# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))                 <---  <class 'numpy.ndarray'>          <-----     O/P 
#
#
# import numpy as np
# arr = np . array ((1,2,3,4,5))
# print(arr)
#
#
# 0-D arrays
# 0-D arrays or scalars are the elements in an element. Each value in an array is a 0-D array 
# import numpy as np
# arr = np.array(42)
# print(arr)
#
# 
# 1-D arrays 
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array
# import numpy as np
# arr=np.array([1,2,3,4,5])                                 This matrix can be represented as [ 1 , 2 , 3 , 4 , 5 ]         1-D array is nothing meant by linear data structure where the elements are stored in linear or straigh forward direction 
# print(arr)
#
#
# 2-D arrays 
# An array that has 1-D arrays as its element is called a 2-D array
# These are often used to represent matrix or 2nd order tensors
# import numpy as np
# arr = np . array ([1,2,3],[4,5,6])                         This matrix can be represented as                                     In 2-D array the the data is stored into matrices 
# print(arr)                                                                               ( [ 1 , 2 , 3 ]        Row 1                                         where this matrices is consist of rows and columns 
#                                                                                            [ 4 , 5 , 6 ] )      Row 2 
#
# 3-D arrays
# An array that has 3-D arrays(matrices) as its elements is called 3-D array
# These are often used to represent a 3rd order tensor 
# import numpy as np 
# arr = np .array (  [      [   [1,2,3] , [1,2,3] , [1,2,3] , [1,2,3]  ] ,
#                           [   [1,2,3] , [1,2,3] , [1,2,3] , [1,2,3]  ]      4 rows 3 columns                This is first face of the matrix    ;      at the back of the front face this is the second face of the matrix 
#                                                                      ]  )    The 3-D matrix can be represented as [   [ 1 , 2 , 3 ]                       [  [ 1 , 2 , 3 ]
# print(arr)    </> arr.shape ---> (2,4,3)  where 2 is the two faces, 4 denotes rows, 3 columns                         [ 1 , 2 , 3 ]                          [ 1 , 2 , 3 ]
#                                                                                                                       [ 1 , 2 , 3 ]                          [ 1 , 2 , 3 ]
#                                                                                                                       [ 1 , 2 , 3 ]  ]                       [ 1 , 2 , 3 ]  ]
#
#
# How to check the dimension 
# import numpy as np 
# a=np.array ( 42 )                           Tensor                                                        # 0-Dimension
# b=np.array ( [ 1 , 2 , 3 , 4 , 5 ] )        1 D array                                                     # 1-Dimension
# c=np.array ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] )          2 D array                                           # 2-Dimension
# d=np.array( [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ] , [ [1 , 2 , 3 ] , [ 4 , 5 , 6 ] ] )    3 D array           # 3-Dimension
#
#
# Higher Dimentsional Arrays
# An array can have any number of dimensions
# when we create an new array we can set how many dimensions it should have to be 
# import numpy as np 
# arr=np.array([1,2,3,4],ndmin=5)
# print(arr)
# print("Number of dimensions",arr.ndim)
#
#
# Accesssing of elements inside the Numerical Array 
# well the access operation which is performed on the list is performed here 
# import numpy as np 
# arr = np . array ( [ 1 , 2 , 3 , 4 ] )
# print( arr [ 0 ] )                       / Accessing of the first element  <-->  Accessing the second element  /      print(arr[1])
# Adding two elements on the numerical array and printing them  --->   print( arr [ 0 ] + arr [ 1 ] )
#
# 
# Accessing of elements inside the 2-D array 
# For to access a element in the 2-D array there are indexes has to passed into square brackets where each of those indexes represent row and column 
#    Column indexes            0   1   2   3   4 
#              arr=np.array( [ 1 , 2 , 3 , 4 , 5 ] ,              0     <--------  row indexes 
#                            [ 6 , 7 , 8 , 9 , 10 ] )             1 
# we are going to access 3rd element on 1st row for this the indexes which are going to be passed in the square brackets are  [ 0 , 3 ]    0 is denotes the row ,  3 represent the column on the row 
#
#
# Accessing of elements inside the 3-D array 
# import numpy as np 
# arr=np.array(  [ [ [ 1 , 2 , 3 ] ,          # Face 1 of the 3-D matrix   ( index based 0) 
#                    [ 4 , 5 , 6 ] ],          
#                  [ [ 7 , 8 , 9 ]            # Face 2 of the 3-D matrix   ( index based 1 )     
#                    [ 10, 11, 12 ] ]  ) 
# 
#                                       Accessing the  11   -->    11 is in face 2 so the index is 1 
#                                       11 is in row 2 on face 2  so the row index is 1 
#                                       on row 2 it is in column 1 (column based index 0,1,2)          
#   print(arr[1,1,1])
#
# 
# Negative Indexing 
# Use negative indexing to access an array from the end 
# import numpy as np
# arr=np.array(  [   [1,2,3,4,5],        This is an 2-D matrix   Row 1
#                    [6,7,8,9,10]  ]  )                          Row 2
# printing the last element in the 2-D matrix 
# print("Last element from the 2-D matrix",arr[1,-1])           1 represents the row and -1 represents the last elements in the row 1 and -2 represents the second last element in the row 2 and -3 to 0 so on .. 
#
#
# Numpy array slicing 
# Slicing array 
# In simple way slicing means taking the sub-list of the original list in a range (start index and end index) inclusive
# the syntax for slicing of array is [start:end]      <----- normal way 
# the syntax for slicing of array is [start:end:step]    <---- step way denotes how many elements we are going to get skipped inbetween the start and end 
# example for step in-purpose 
# indexes =   0   1   2   3   4    5   6   7   8   9    10   11   12   13   14   15
#     arr = [ 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 ]
# print(arr[3:10:2]) 
#                         4            7           10       This are elements will get printed 
#                             1    2       1   2            This are step values which is used to skip the elements 
# 
# import numpy as np
# indexes    :    0 1 2 3 4 5 
# arr = np.array([1,2,3,4,5,6])
# print(arr[3:])                           O/P --> [ 4 , 5 , 6 ]   from the index 3 the elements will get printed 
#
#
# import numpy as np
# indexes    :    0 1 2 3 4 5 
# arr = np.array([1,2,3,4,5,6]) 
# print(arr[:4])                           O/P --> [ 1 , 2 , 3 ,4 ]  from the index 0 to the end of index 4 (before 4 the printing of elements will get stopped)
#
# 
# import numpy as np
# indexes    :      0   1   2   3   4   5   6
# -indexes   :     -7  -6  -5  -4  -3  -2  -1      
# arr = np.array( [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] )       
# print(arr[-3,-1])                        O/P --> [5.6]     -3 -2 -1 at before -1 the printing of elements will get stopped 
# 
#
# Returning the every elements of the array but with step 2 
# arr = np.array([1,2,3,4,5,6,7])
# print(::2)          --> O/P       [ 1 , 4 , 7 ]
#
#
# Slicing 2-D array 
# arr = np . array (  [  [ 1 , 2 , 3 , 4 , 5 ],
#                        [ 6 , 7 , 8 , 9 , 10]  ]  )
# print(arr[1,1:4])    1 represents row 1 
#                      1:4 represents the column value of row where 1st column to 4th-1 column 1st row elements will get printed 
#                      O/P  --> [ 7 , 8 , 4  ]
# 

