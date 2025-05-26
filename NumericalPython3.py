# Numerical Python Iteration 
# Iteration means going through the array elements one by one
# To traverse an any dimensional array we can simply use FOR loop
# Below is an example program for to access the elements inside the numerical array 
#
#
# import numpy as np
# arr = np.array( [ 1 , 2 , 3 ] )
# for element in arr : 
#      print( element )
#
#
# To access the values in 2-D array, we should have to two loops -> outer loop for the rows and inner loop for the column elements of that array 
# import numpy as np
# arr = np . array ( [ [ 1 , 2 , 3 ],   
#                      [ 4 , 5 , 6 ]  ]  )
# for row in arr :                     
#     for column in row:
#           print( column,end=' ' )      <-- The 2-D matrix will be printed 
#
#
# To access the eleements in the 3-D array, we should have to use three loop
# One is for face of the matrix, Second loop is for face row and third loop for the row's column 
# arr=np.arr( [  [ [ 1 , 2 , 3 ] , [ [ 1 , 2 , 3 ] ,
#                  [ 1 , 2 , 3 ] ],  [ 1 , 2 , 3 ] ]   ]  )
# for face in arr :
#      for row in face :
#           for column in row : 
#                   print( column , end=' ' )
# 
#
# Iterating Arrays using nditer()
# nditer() is a function that can be used from very basic to very advanced iterations
# When we use for loop to iterate over an array specifically 2-d or 3-d we should have to use n loops acording to it
# 
# Below is python program that uses nditer() to iterate over the array and print the elements 
# arr=np.array( [   [ [ 1 , 2 ] , [ 1 , 2 ] ] ,
#                   [ [ 5 , 6 ] , [ 7 , 8 ] ]   ])
# for element in np.nditer(arr):               <-------- In here we are using the np module and nditer() through the dot operator and passing the arr array inside the loop 
#       print( element )
#
#
# Iterating array with different data types 
# There is an method where we can change the data type of the array and print it in the execution of the program
# arr=np.array( [ 1 , 2 , 3 ] )
# for element in np.nditer( arr , flags = [ 'buffered' ] , op_types=['S'] ) :                  <--- op-types represent the type of object we needed to print from its original tpye , flags is used to define them as it was buffered 
#       print(element)
#
# 
# Iterating the array elements by skipping the values inside them while at the time of printing 
# arr = np . array([[1,2,3,4],[5,6,7,8]])
# for element in np.npiter(arr[:,::2]):       1 2 3 4 5 6 7 8  -->  1 4 7 
#        print(element)                         - -   - -   - 
#
#
# Enumerate : Enumerate can de stated as when we want index element to get printed with the array elements 
# arr = np . array([1,2,3])
# for index,element in np.ndenumerate(arr):
#       print(index," ",element)                      ---->       0 1    1 2    2 3 
#
#
# Concatenation of two numerical python arrays 
# In this library concatenation operation we are going to concatenate according to the equal match of there axes 
# axes means dimension of the array 
# Both the array1 and array 2 should match the dimension of each others, if not concatenation of the two arrays will provide errors 
# Different length with same dimension could be concatenated but with same lenght different dimensions could not be added together  
#
# arr1=np.array([1,2,3])            <-- arr1 with the length of 3 and same dimension  
# arr2=np.array([4,5,6])            <-- arr2 with the length of 3 and same dimension
# arr=np.concatenate((arr1,arr2))   <-- same length does not provide any error 
# print(arr)                 O/P --->[ 1 , 2 , 3 , 4 , 5 , 6 ]
#
# arr1=np.array( [ 1 , 2 , 3 ] )
# arr2=np.array( [ 4 , 5 , 6 , 6 ] ,
#                [ 7 , 8 , 9 , 0 ] )  
# arr=np.concatenate(arr1,arr2)        <-- Provides error here
#
#
# Joining two 2-Dimensional array along rows (axis=1)
# arr1=np.array(  [ [ 1 , 2] , [ 3 , 4 ] ]  )
# arr2=np.array(  [ [ 5 , 6],  [ 7 , 8 ] ]  )
# arr = np.concatenate( ( arr1 , arr2 ) , axis = 1 )
# print(arr) 
#
#
# Joining 2 array using stack, stack is an data structure used for recursion
# Stacking is like keeping the concatenating array on the top of the other array 
# Concatenating two-1-D arrays , with the second axis this would result in putting them one over the other
# Syntax for stack ---> np.stack((arr1,arr2),axis=1)
# print(arr) 
# arr1 = np . array ( [ 1 ,2 , 3 ] )         # Both the array is rotated 90 degree towards the rigth 
# arr2 = np . array ( [ 4 ,5 , 6 ] )         # The rows are converted into column, the columns are being converted to rows 
# O/P :  [[1 4]
#         [2 5]
#         [3 6]]
#
#
# Stacking along columns                      <--- Stacking : simply by using the stack() we are rotating the array 90 degrees
# arr1=np.array([1,2,3])                      <--- By using Vstack we are concatenating both of them without the need of rotating of the array to 90 degrees and we are concatenating the column to get converted into rows 
# arr2=np.array([4,5,6])
# arr=np.vstack((arr1,arr2))
# print(arr)                                  <--- [ 1 , 2 , 3
#                                                    4 , 5 , 6 ]
#
#
# Splitting of an array is nothing but dividing the array into two parts by using the index as the arguments ; the method is used here is split(arr,argument)
# arr = np . array ( [ 1 , 2 , 3 , 4, 5 , 6 ] ) 
# newarr = np . array_split( arr , 3 )              
# print(newarr)                    |______________---->  Divides tbe array into 3 parts 
#                                                 ---->  If it is four then the array will get divided into 4 parts      ---> 1,2  3,4  5,6 
#
# Splitting 2-D arrays 
# Same function is here too
# arr = np . array( [ [ 1 , 2 ] ,
#                     [ 3 , 4 ] ,
#                     [ 5 , 6 ] ,             7 rows , 2 columns  is converted into 4 rows 2 columns 
#                     [ 7 , 8 ] ,
#                     [ 9 , 10 ] ,
#                     [ 11 , 12 ] ,
#                     [ 13 , 14 ] ] )
# new_arr = np . array_split ( arr , 4 )
# print(new_arr)                 O/P --->  [ array ( [ [ 1 ,  2 ] , [ 2 , 4 ] ] ),
#                                            array ( [ [ 5 ,  6 ] , [ 7 , 8 ] ] ),
#                                            array ( [ [ 9 , 10 ] , [ 11, 12] ] ),
#                                            array ( [ [ 13, 14 ] ] ) ]               <----- The array is divided into four rows, meanwhile the np.split requires the array to be split evenly on par with the np.array_split() handles uneven splits 
#
# arr = np . array( [ [ 1 , 2 ] ,
#                     [ 3 , 4 ] ,
#                     [ 5 , 6 ] ,
#                     [ 7 , 8 ] ,
#                     [ 9 , 10 ] ,
#                     [ 11 , 12 ] ,
#                     [ 13 , 14 ] ] )
# new_arr = np . array_split ( arr , 3 )
# print(new_arr)                 O/P --->  [ array ( [ [ 1  ,  2 ] ,
#                                                      [ 3  ,  4 ] ,
#                                                      [ 5  ,  6 ] ] ),      <--- Splitting the 2-d array with specified as 3 rows in the array_split but with different columns no 
#                                            array ( [ [ 7  ,  8 ] ,
#                                                      [ 9  , 10 ] ] ),
#                                            array ( [ [ 11 , 12 ] ,
#                                                      [ 13 , 14 ] ] ) ]
#
#
# arr = np . array ( [ [ 1 , 2 , 3 ] ,
#                      [ 4 , 5 , 6 ] ,
#                      [ 7 , 8 , 9 ] ,                array with 6 rows and 3 columns 
#                      [ 10 , 11 , 12 ] ,
#                      [ 13 , 14 , 15 ] ,
#                      [ 16 , 17 , 18 ] ] )
# newarr = np . array_split ( arr , 3 , axis = 1 )      <--- By using axis=1, we are converting row into columns or columns into rows, i.e split the 3 columns into 3 parts [splitting along columns], columns in to 3 parts ! 
#
# print(newarr)                O/P  --->  [ array ( [ 1 ]  ,
#                                                   [ 2  ] ,
#                                                   [ 3 ] ,
#                                                   [ 4 ] ,
#                                                   [ 5 ] ,
#                                                   [ 6 ] ),
#                                           array ( [ 7 ] ,
#                                                   [ 8 ] ,
#                                                   [ 9 ] ,
#                                                   [ 10 ] ,
#                                                   [ 11 ] ,
#                                                   [ 12 ] ),
#                                           array ( [ 13 ] ,
#                                                   [ 14 ] ,
#                                                   [ 15 ] ,
#                                                   [ 16 ] ,
#                                                   [ 17 ] ,
#                                                   [ 18 ] ) ]
#
# Explanation of axis in np.array_split()                    <-- Below specifications are for 2-D matrix 
# axis = 0    splitting the rows( vertical split )
# axis = 1    splitting the columns( horizontal split )
# 
