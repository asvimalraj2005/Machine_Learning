# Data Types in Python
# strings --> used to represent text data within double quotes where character can be wrapped around within single quotes 
# integer --> + infinity to - infinity
# float   --> decimal point numbers 
# boolean --> True or False will represented 
# complex --> Real number representation or complex number representation  -->  1.0 + 2.0 i
#
#
# Data Types in numerical python 
# Numerical python has some extra data types, and refer to data types with one character, like i for integers and, u for unsigned integers 
# There are lot of data types are there but only one type is used to create a numerical python array 
# i - integer                                      -->   array contains -infinity values to +infinity values
# b - boolean                                      -->  array contains 0's and 1's   -> 1 to +infinity represents True and 0 to -infinity represents False
# u - unsigned integer                             -->   array contains 32-bit datum that encodes a non-negative integer in the range [0 to 4294967295]
# f - float                                        -->  array contains of decimal values 
# c - complex float                                -->  array contains of imaginary values 
# m - timedelta                                    -->  array contains of data that have the duration between two events 
# M - datetime                                     -->  array contains of data and time values (IDK )
# O - object                                       -->  array contains of Object which is created in runtime
# S - String                                       -->  "double quoted character or sequence of character enquoted within double quotes and seperated by comma's on a numerical array "
# U - unicode string                               -->  Unicode can be stated as ASCII values where it is helpful in representing special characters and what are the symbols on the keyboard
# V - fixed chunk of memory for other type (void ) -->     Hmm fixed chunk of memory -> Only a limited amount of bytes can be stored on the numerical python array 
#
# From the above data types that main datatypes that are used in common or in general programming are i , b , u , f , c , o , s 
#
# import numpy as np
# arr = np . array ( [1,2,3,4] )
# print(arr.dtype)                    ---> O/P    i
#
#
# import numpy as np 
# arr = np . array (['apple','banana','Octopus'])
# print(arr.dtype)                    ---> O/P    S 
#
#
# import numpy as np                                                                                                                                                   String and then byte string 
# arr = np . array ([1,2,3,4],dtype='S')     --> Here the conversion happens where the integer that are in the numerical array is converted into byte strings  -->  1=> '1' => b'1'   
# print(arr)                           O/P   --> b'1' ,b'2' ,b'3' ,b'4' 
# print(arr.dtye)                                |S1
#
#
# import numpy as np 
# arr = np . array ([1,2,3,4],dtype='i4')    -->  Creating the array with 4 bytes integer ( 32 bit signed integer [-2^32 to 2^31])
# print(arr)                                 -->  printing the numerical array 
# print(arr.dtype)                           -->  printing it's type i.e i4
#
#
# Let's clear the confusion of i4 
# Below is the table on the usage i4, i8, i16, i32, i64 
#  Numerical Python Type                Name                Bytes               Value Range (Signed means negative to positive or vice versa)
#       i1                              1                   8                   -128 to 127
#       i2                              2                   16                  -32,768 to 32,767
#       i3                              4                   32                  -2^32 to 2^31
#       i4                              8                   64                  -2^64 to 2^64
#
#
# Note : if a value is not being getting converted from it's original type to it's defined type by the user than the program will be provide the output as ValueError
#
#
# Converting Data type on existing arrays 
# Process involved in converting the existing data type of an array to other array is create a seperate numerical array
# by using astype() we can copy the original numerical array elements to the duplicate array where the same format will be represented on the duplicate array too 
# to change the format we must use data types as arguments in the astype() --> by passing the arguments to the astype() it will look like this astype(int), astype(bool) ect 
# 
#
# Copy vs View 
# Copy function copies entire object value and if we change anything to the duplicated array it will not affect the original array 
# View function is used to view the array, the modification done to the view function array will get reflected on the original array 
#
# import numpy as np
# arr = np . array ( [ 1 , 2 , 3 , 4 , 5 ] )           # New array is created here with the name of arr 
# x = arr . copy()                                     # Another new array is created with the name of x
# arr[0] = 50                                          # Now we are modifying the index 0th element on the arr array -> now arr will be look like this [ 50 , 2 , 3 , 4 , 5 ]
# print(arr)                                           # printing the modified arr array 
# print(x)                                             # printing the non-modified x array, where the original arr will not reflect any changes on the x array 
#
#
# Now we are moving to View method
# The original array modificatio will be reflected in the x array 
# The x array modification will be reflected in the arr original array 
#
# import numpy as np
# arr = np . array([1,2,3,4,5])                        # Creating an new array named arr with values contained in it 
# x = arr . view ()                                    # x is an array where the x object is directed to the arr object , both of them will represent the same values , if any side the change is happened then it will get reflected on both 
# x[0] = 40                                            # 0th index is changed from 1 to 40
# print(arr)                                           # Printing both of the arrays -> 40,2,3,4,5
# print(x)                                             #                             -> 40,2,3,4,5
#
# 
# Copy function creates new object with values and assigns to the new variable, when we check it by using the base method it returns None because it does not dependent on any object it does dependent on it's own 
# View function -> one is main object and other one is duplicate object, the view returns the original array 
#
#
# import numpy as np 
# arr = np.array([1,2,3,4,5])
# x=arr.copy()                          
# y=arr.view()
# print(x.base)                     --> Returns None
# print(y.base)                     --> Returns the original array because it does dependent onto the original array 
#
#
# Shape of an Array
# The shape of an array is the number of elements in each dimension like 1-D or 2-D or 3-D 
# To get the shape of an array we can simply use the shape method that returns the array shape inside a tuple.
# if it is only one value based tuple it is considered as a tensor or 1-D array 
# if it is two value based tuple then it is considered as 2-D array 
# if it is three based tuple then it is considered as 3-D array 
# Below is an example 
# 
# import numpy as np
# arr = np.array([  [1,2,3,4,5],
#                   [6,7,8,9,10]  ] )
# print(arr.shape)
#
#
# Reshaping --> Reshaping means changing the shape of the array from 1D to 2D or many (Cardinality)
# Through this kind of process we can simply change the dimensions of the array by adding dimensions or removing it 
# Let us take an example
# import numpy as np                               
# arr = np . array ([1,2,3,4,5,6,7,8,9,10,11,12])               # to reshape this array the product of dimension that the user wants is be equal to the total no elements in the array of the array          
# newarr=arr.reshape(4,3)                                       # 2,6    2-D
# print(newarr)                                                 # 4,3    2-D
#                                                               # 2*3*2  3-D
#                                                               # 3*2*2  3-D
#                                                               # 1*3*4  3-D
# Reshaping an 1-D array to 3-D array 
# 3-D array consist of faces (4,5,6)  where 4 represents the face , 5 represents the no of rows in each face , 6 represents the no of columns on each row                                                                                                                                                                                                  
# import numpy as np                                                                                                                                                                                           
# arr = np . array ([1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12])     # In here there are 24 elements 
# newarr=arr.reshape(3,2,4)                                                      # Dimension products like 6  *  2  *  2 
# print(newarr)                                                                                            1  *  12 *  2
#                     Now the newarr will have 3 faces, 2 rows, 4 columns                                  12 *  1  *  1               
#                      ([ [[1,2,3,4],          [[9,10,11,12],     [[5,6,7,8],                              2  *  3  *  2        
#                          [5,6,7,8]],          [1,2,3,4]],        [9,10,11,12]]  ])                       3  *  2  *  2             
#                          First Face           Second Face         Third Face                             1  *  3  *  4                                                                   
#                                                                                                    
#
# Note : Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension(will raise an error)
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])        The arr has total 8 elements 
# newarr=arr.reshape(3,3)                3*3 product equal 9 , one element is missing to create an new array so it will raise valueError 
# print(newarr)                          
#
# You can add -1 to any one of the following dimensions where if you don't know any dimension to get passed as argument to the reshape function 
# 
#
# Flattening the arrays 
# Flattening the arrays means we are converting any multi dimensional array to an 1-D array 
# For Flattening we can use array.reshape(-1)
# Let us take an example 
# import numpy as np 
# arr=np.array([1,2,3],[4,5,6])
# newarr=arr.reshape(-1)              O/P : ([1,2,3,4,5,6])
# print(newarr)
