# Stastistics variance
#  Duration	        Average_Pulse	           Max_Pulse	Calorie_Burnage	   Hours_Work	Hours_Sleep 
      30	              80                     	120	                240	          10	     7
      30	              85                    	120             	250           10         7 
      45	              90                    	130	                260         	8	     7
      45                 	95	                    130	                270	            8        7
      45               	100                     	140             	280         	0       	7
      60	            105                     	140	                290           	7	      8
      60	            110                      	145	                300          	7       	8
      60	            115                     	145	                310          	8	      8
      75             	120	                        150             	320	            0       	8
      75            	125	                        150               	330         	8       	8

# Step 1 to Calculate the Variance: Find the Mean
# We want to find the variance of Average_Pulse.

#1. Find the mean:
 
# (80+85+90+95+100+105+110+115+120+125) / 10 = 102.5
# The mean is 102.5
# 2. Find the difference from the mean for each value:
#
# 80 - 102.5 = -22.5
# 85 - 102.5 = -17.5
# 90 - 102.5 = -12.5
# 95 - 102.5 = -7.5
# 100 - 102.5 = -2.5
# 105 - 102.5 = 2.5
# 110 - 102.5 = 7.5
# #115 - 102.5 = 12.5
# 20 - 102.5 = 17.5
# 25 - 102.5 = 22.5

# Step 3: For Each Difference - Find the Square Value
# 3. Find the square value for each difference:

# (-22.5)^2 = 506.25
# (-17.5)^2 = 306.25
# (-12.5)^2 = 156.25
# (-7.5)^2 = 56.25
# (-2.5)^2 = 6.25
# 2.5^2 = 6.25
# 7.5^2 = 56.25
# 12.5^2 = 156.25
# 17.5^2 = 306.25
# 22.5^2 = 506.25
# Note: We must square the values to get the total spread
#
# Step 4: The Variance is the Average Number of These Squared Values
# 4 . Sum the squared values and find the average:
#
# (506.25 + 306.25 + 156.25 + 56.25 + 6.25 + 6.25 + 56.25 + 156.25 + 306.25 + 506.25) / 10 = 206.25
# The variance is 206.25.
# Example
# import numpy as np
#
# var = np.var(health_data)
# print(var)
#
# Example of a Perfect Linear Relationship (Correlation Coefficient = 1)
# we will use scatterplot to visualize the relationship between Average_Pulse and Calorie_Burnage (we have used the small data set of the sports watch with 10 observations).
#
# This time we want scatter plots, so we change kind to "scatter":

# Example
# import matplotlib.pyplot as plt
# 
# health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter')
# plt.show()
#
#
# Example of a Perfect Negative Linear Relationship (Correlation Coefficient = -1)
# Correlation Coefficient = -1
# We have plotted fictional data here. The x-axis represents the amount of hours worked at our job before a training session. The y-axis is Calorie_Burnage.
#
# If we work longer hours, we tend to have lower calorie burnage because we are exhausted before the training session.
#
# The correlation coefficient here is -1.
#
# Example
# import pandas as pd
# import matplotlib.pyplot as plt
# 
# negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
# 'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
# negative_corr = pd.DataFrame(data=negative_corr)
#
# negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')
# plt.show()
