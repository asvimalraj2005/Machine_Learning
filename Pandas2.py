# Pandas - Fixing Wrong Data
# Wrong Data : If you take a look at out data set, you can see that in row 7, the duration is 450, but for the all the other duration is between 30 and 60 
#   
#       Duration   Date        Pulse  Maxpulse  Calories
#  0         60  '2020/12/01'    110       130     409.1
#  1         60  '2020/12/02'    117       145     479.0
#  2         60  '2020/12/03'    103       135     340.0
#  3         45  '2020/12/04'    109       175     282.4
#  4         45  '2020/12/05'    117       148     406.0
#  5         60  '2020/12/06'    102       127     300.0
#  6         60  '2020/12/07'    110       136     374.0
#  7        450  '2020/12/08'    104       134     253.3
#  8         30  '2020/12/09'    109       133     195.1
#  9         60  '2020/12/10'     98       124     269.0
#  10        60  '2020/12/11'    103       147     329.3
#
# How can we fix values, like the one for "Duration" in row 7 
# Replacing Values -> It is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7
#
# --> df.loc[ 7 , 'Duration' ] = 45
# 
# For small data sets you might be able to replace the wrong data one by one, but not for big data sets 
# To replace wrong data for larger data sets you can create some rules, e.g set some boundaries for legal values, and replace any values that are outside of the boundaries 
# 
# Loop through all values in the "Duration" column : 
# for x in df.index :                                               <-- Loop through all values in the "Duration" column 
#       if df.loc[x,"Duration"]>120:                                <-- If the values is higher than 120, set it to 120 
#            df.loc[x,"Duration"] =120
# 
# 
# Removing the rows which consist of wrong data
# for x in df.index:
#       if df.loc[x,"Duration"]>120:
#           df.drop(x,inplace=True)
#
# Removing the duplicates 
# Duplicates are nothing but the replicated values will be shown twice or multiple times 
#  
# print(df.duplicated())   --> Returns True for evert that is a duplicate, otherwise False
# 
# To remove duplicacies 
#   df.drop_duplicates( inplace = True )
#   The inplace = True states that will make sure it will remove all the duplicacies in the dataframe without creating the new data frame 
# 
# Data Correlations
# Finding relationships 
# corr() method is used to find the relationship between any two values 
# df.corr()
# 
# Good correlation : Nearer to one(1)   0.92345
# Bad correlation : Farer to one(1)     0.00083
#
# Scatter Plot 
# kind = 'scatter'
# A scatter plot needs an x-axis and y-axis 
# 
# import pandas as pd 
# import matplotlib.pyplot as plt
# df=pd.read_csv('data.csv')
# df.plot(kind='scatter',x='Duration',y='Calories')
# plt.show() 



