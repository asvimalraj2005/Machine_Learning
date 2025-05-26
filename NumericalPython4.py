# Searching an element inside the array 
# To search an element in the numerical python array we must pass the value as the argument in the where() function
# This is how the syntax looks like for the where function()  -->  index_variable = np . where ( arr = 4 )
# index_variable now stores the indexes of the element which is present inside the array and if not it will return 0 
# 
# Below is an example on how the numpy array where function() working
# array_1 = np . array ( [ 1 , 2 , 3 , 4 , 5 , 4 , 4 ] )
# element_indexes = np . where ( arr == 4 )
# print( elemenet_indexes )           <--- The output example looks like this ( array ( [ 3 , 5 , 6 ] ) )
#
# Find the indexes of the elements which is divisible by 2 or the remainder should equals to zero when the number is getting divided by zero
# arr = np . array ( [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ] )
# even_indexes = np . where ( arr % 2 ==0 )
# print( even_indexes )
#
# Find the indexes of the elements which are not divisible by 2 or the remainder should equals to 1 when the elements are getting divided by 2 
# arr = np . array ( [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ] )
# odd_indexes= = np . where ( arr % 2 == 1)
# print( odd_indexes )
#
# We can start the searching of element from any two sides which is right side and left side 
# Below is the program which defines on how to use the right side searching and left side searching function 
# arr = np . array ( [ 6 , 7 , 8 , 9 ] ) 
# element_index = searchsorted(arr,6,side='right')      <-- This will start the search from the right of the array 
# element_index = searchsorted(arr,6,side='left')       <-- This will start the search from the left of the array 
#
# SearchSorted() function is used to return the value of the indexes where the element should have to get inserted 
# arr = np . array ( [ 6 , 7 , 8 , 9 ] )
# element_index = np . searchsorted(arr,7)
# print(element_index) --> returns the index 1 the elements from the index 1 are right shifted 
#
# Numerical pytoon order the elements in ascending order 
# To dynamically sort the array without using predominantly with the typed code then we can use sort()
# sort() function is a library, which is used to order the elements inside them in a ascending way, where each element to the right adjacent for every element will be greater than it's own element 
# arr = np . array ( [ 3 , 2 , 0 , 1 ] ) 
# print(np.sort(arr))        <-- The original array is not modified only the array is modified and printed only inside the print statement not externally in the array 
# 
# We can sort the string values containing array, boolean value containing array 
# arr = np . array (['banana','cherry','apple'])     
# print(np.sort(arr))                       <--- Lexicographical order the strings are will get sorted 
#
# arr = np . array ([True,False,'False'])
# print(np.sort)                            <--- False,True,True
#
# Filtering arrays 
# Removing some elements from the array and returning a new array is called as filtering 
# If the value at an index is True that element is contained in the filtered array
# If the value at that index is False that element is excluded from the filtered array 
# Creating an array from the elements on index 0 , index 2 , index 4 
# arr = np . array ( [ 1 , 2 , 3 , 4 , 5 ] )                           
# boolean_value = [ True , False , True , False , True ]                  <---- Here are the boolean values are mapped to the value according to the index based , If boolean_array has True in index 0 then the origial array index element will be added to the new array 
# new_arr = arr [ boolean_value ]  
# print( new_arr )                           
#
# Creating an filter array that will return only even elements from the orignal array 
# import numpy as np
# arr = np . array ( [1,2,3,4,5,6,7])           <--- Creating an new array named arr with values containing in them 
# filter_arr = []                               <--- Creating an nee array named 'filter_arr' which is used to store the boolean values 
# for element in arr :                          <--- By using the for loop we are traversing the elements in the arr    
#       if element % 2 == 0 :                   <--- If the element in the arr is even then the filter_arr will be added with True 
#           filter_arr.append(True)
#       else : 
#           filter_arr.append(False)            <--- Else the False is added to the filter_arr
# newarr = arr[filter_arr]                      <--- Creating the new_arr with elements containing in them where the filter arrays looks like this True,False,True,False,False,False,True ; The True and False stands with index and the condition whether the value in the original array of the same index as filter array is added in the new_array or not 
# print(filter_arr)
# print(newarr)

