# Matplotlib Scatter
# Scatter plot is one of the important plot in Machine Learning 
# The scatter() function plots one dot for each observation i.e x1 and y1 meeting point 
# Below is the example python code for the matplotlib 
#
# import matplotlib.pyplot as plt
# import numpy as np
# A1 = np . array ( [  5  ,  7  ,  8  ,  7  ,   2  ,  17  ,  2  ,  9  ,  4  ,  11  ,  12  ,  9  ,  6  ] )
# A2 = np . array ( [  99 ,  86 ,  87 ,  88 ,  111 ,  86  , 103 ,  87 ,  94 ,  78  ,  77  ,  85 ,  86 ] )
# plt.scatter( A1 , A2 )      <---  Two arrays are passed here one with x values and another with y values 
# plt.show()
#
# Below is an example for comparing the plots and each of the seperate arrays will have different colour
# import matplotlib.pyplot as plt 
# import numpy as np
# X_Axis_Point = np . array ( [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ] )
# Y_Axis_Point = np . array ( [ 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0 , 11 , 12] )
# plt.scatter( X_Axis_Point , Y_Axis_Point , color='red' )
# X_Axis_Point_1 = np . array ( [ 0 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 11 , 12 ] )
# Y_Axis_Point_2 = np . array ( [ 5 , 4 , 3 , 2 , 1 , 6 , 7 , 8 , 9 , 0 , 11 , 12 ] )
# plt.scatter( X_Axis_Point_1 , Y_Axis_Point , colot='blue' )
# plt.show()
# 
# Matplotlib has an sub library named bar()
# bar() function chart is used to draw bar graphs 
# import matplotlib.pyplot as plt 
# import numpy as np
# X_Axis_Points = np . array (["A","B","C","D"])
# Y_Axis_Points = np . array ([ 3 , 8 , 1 , 19 ])
# plt.bar(X_Axis_Points,Y_Axis_Points , color='r' ,  width = 0.1 )                    or                   plt.barh(X_Axis_Points,Y_Axis_Points)   <---  This line is used to draw the bar chart in horizontal way 
# plt.show()
#
