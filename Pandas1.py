# Pandas vs Numerical Python 
# Pandas is mainly used for reading CSV files , Filling missing values , Labelling purpose , Cleansing ect (Data Analysis )
# Numerical Python is for powerful calculation of different types of tensors or scalars or 2-D or N-D dimensions of data (Scientific Computing )
# >>>>>> pip install pandas 
# Base 
# import pandas as pd 
# df = pd . read_csv ( ' data . csv ')
# print( df . to_string ( ) ) 
# 
# The above 3 lines is base for reading every kind of csv files with any limit of data 
# 
# as straight away without using any pandas 
#                                                  <> <> Dictionary is an data structure where the data is stored in the format of keys and values , where each key is linked with value or values. 
# import pandas                                    <--- Importing the pandas library
# mydataset = {                                    <--- Creating a dictionary
#       'cars' : ["BWM","Volvo","Ford"],           <--- key 'cars' has values of "BWM" , "Volvo" , "Ford"    
#       'passing' : [ 3 , 7 , 2 ]                  <--- key 'passing' has values of 3 , 7 , 2 
# }                                                    
# myvar=pandas.DataFrame(mydataset)                <--- Passing the mydataset data structure in pandas DataFrame for creating a new DataFrame
# print(myvar)                                     <--- Printing the values inside the converted dataframe 
#
# Series function in pandas 
# import pandas as pd
# a = [ 1 , 7 , 2 ]
# myvar = pd.Series(a)               # A series is like a column in a table 
# print(myvar)                       # It is a one-dimensional array holding data of any type 
#                  O/P :  0   1
#                         1   7
#                         2   2 
#                        dype: int64  
#                                           where 0 1 2 are indexes are associated with the values in the array 
# 
# Labels : For not want to print the indexes we should have to create a new array with labels consisting that relates with original array value until it reaches the original length array 
# a = [1,7,2]
# myvar=pd.Series(a,index=["A","B","C"]) 
# print(myvar)                          
#              (or)
# a = [1,7,2]
# index=["A","B","C"]
# myvar=pd.Series(a,index) 
# print(myvar)                                   O/P :  A  1   
#                                                       B  7
#                                                       C  2
#                                                   dtype: int64
#
# By referring to the variable in the index we can able to retrieve the data of it 
# 
# Key / Value object as Series 
# By using dictionary or any other data type we can easily able to create series
# 
# import pandas as pd 
# timeline = {"2036":1 , "2040": 10, "2045":5}
# myvar=pd.Series(timeline)                                   or                myvar = pd.Series(timeline,index=["2036","2040"])
# print(myvar)
#                                               O/P : 2036  1 
#                                                     2040  10  
#                                                     2045  5
#                                                     dtype : int64 
#
# Series is like a column 
# DataFrame is the whole table 
# Data sets in pandas are usually multi-dimensional tables called DataFrames
# 
# import pandas as pd 
# data = { "timeline" : [ 2036 , 2040 , 2045 ],
#                       [   1  ,  10  ,  5   ] }
# myvar = pd.DataFrame(data)
# print(myvar)
#
#
#
#
