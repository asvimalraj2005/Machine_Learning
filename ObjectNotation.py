# Object Notation files in general are used as data carrying containers medium where the data stored inside as keys and values or any other format
# There are different types of Object Notation and Object transferring medium, 
# JSON is a plain text, but has the format of an object, and is well known in the backend development, transferring the data between the clients and users  
# In the below example we are going to use the file named as data1.json
# import pandas as pd
# df=pd.read_json('data1.json')        <--- read_json is an function used to convert the JSON files into data frames 
# print(df.to_string())                <--- Prints the entire dataframe
#
# JSON format is same as dictionary 
# import pandas as pd 
# data = { "Timeline":{"2036":1,
#                      "2040":10,
#                      "2045:5"},
#          "Date": {"2036":1,
#                   "2040":10,
#                   "2045":5},
#        }
# df = pd.DataFrame(data)
# print(df )
#
#
# Pandas - Analyzing DataFrames 
# Viewing the Data  -->  head() function used to return the top 5 rows in a dataset if any parameters mentioned inside the parenthesis then according to the value passed inside the parenthesis the dataframe rows will get printed 
# print(df.head(10))  -->  First ten rows
# print(df.head())    -->  first 5 rows 
# print(df.tail())    -->  Last 5 rows 
# print(df.info())    -->  The information of the dataframe will be printed here 
#
#
# Data Cleansing 
# Data Cleansing --> Empty cells , Data in wrong format , Wrong Data , Duplicates 
# 
# The data set <Blank> ? 
#
# Duration          Date  Pulse  Maxpulse  Calories
# 0         60  '2020/12/01'    110       130     409.1
# 2         60  '2020/12/03'    103       135     340.0
# 3         45  '2020/12/04'    109       175     282.4
# 4         45  '2020/12/04'    109       175     282.4
# 5         60  '2020/12/06'    102       127     300.0
# 6         60  '2020/12/07'    110       136     374.0
# 7        450  '2020/12/08'    104       134     253.3
# 8         30   2020/12/09     109       133     Nan
# 9         60  '2020/12/10'     98       124     269.0
# 10        60          Nan     103       147     329.3
#
#     
# --> Empty Cells : Empty cells can potentially give you wrong result when you analyze data 
# --> Due to empty cells present inside the data we should remove the entire data 
# --> Removal misconception is true : for larger data analysing does not create any variation in big difference 
#                                     for smaller data the analysing of data create bigger variation while in the process of analysing the data 
# steps involved : below lines of code are used to remove the empty cell rows on the entire dataset 
# import pandas as pd               <--- Importing pandas as pd 
# df = pd.read_csv('data.csv')      <--- Reading the CSV files by using read_csv method and storing into df object 
# new_df=df.dropna()                <--- dropna() is a function is used to remove the cells with empty values or Null values and new dataframe is stored into new_df 
# print(new_df.to_string())         <--- printing the entire dataframe 
#
#
# without creating another dataframe just directly removing the dataframe values itself 
# import pandas as pd 
# df = pd . read_csv('data.csv')                        <-- Reading the data file 
# df = dropna( inplace = True )                         <-- Changing the file within itself and storing within the object itself 
# print( df . to_string ( ) )                           <-- Making to print the entire data frame
#
# Replacing the empty values is filling it with a values 
# import pandas as pd                       
# df = pd.read_csv('data.csv')                      
# df.fillna(130,inplace=True)                            <-- Filling all the rows and columns empty value with the value of 130 
# 
# Replacing the Null values in the any column you want with the value 1 or an preferrable value
# import pandas as pd 
# df = pd . read_csv ('data.csv') 
# df.fillna({"Column":130},inplace=True)                 <-- Filling only one specific column which contains any missing values then the column value will get filled as 130 
#
# Replace the empty values through by calculating the mean, median or mode
# impirt pandas as pd 
# df = pd.read_csv('data.csv') 
# x = df ["column"].mean()                                          # Calculating the column mean value and replacing the empty value with the mean value 
# df.fillan({"column":x},inplace=True)                              # Replacing the null values with x value through 'fillan' method 
