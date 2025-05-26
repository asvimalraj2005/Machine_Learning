# Matplotlib is an sub library of pyplot, which is mainly used for visualising of data 
# Matplotlib is always imported under the name of plt inside the python program
# Below is a example program of how the graph are generated through pyplot library 
# 
# import matplotlib.pyplot as plt                 <--- Importing the matplotlib library 
# import numpy as np                              <--- Importing the numerical python library 
# A_points = np . array ([ 0 , 6 ])               <--- Creating array one A with x axis point and x1 axis point ; where A's 0 represent x and A's 6 represent x1
# B_points = np . array ([ 0 , 250])              <--- Creating array two B with y axis point and y1 axis point ; where B's 0 represent y and B's 250 represent y1 
# plt.plot(A_Points,B_Points)                     <--- while in the process of plotting the x1,y1 creates a one point in the chart and x2,y2 creates a second point in the chart 
# plt.show()
#
# Below is how the chart is shown
#       250 - |                  /
#             |                /
#       200-  |               /
#             |             / 
#       150-  |           / 
#             |         / 
#       100-  |       /
#             |     /
#       50-   |   / 
#             | /
#       0-    |/________________________       <----- X axis
#                   
#               0  1  2  3  4  5  6              From 0 to 250 on the x axis and y axis 
#           
#           ^
#           |  
#           This is y axis 
#
# Matplotlib plotting : the plot () is draw lines from one point to another point 
# This function takes two parameters as input 
# Parameter 1 is an array containing the points on the x-axis 
# Parameter 2 is an array containing the points on the y-axis 
# For an clear example if we need to draw line from an point with the values of (1,3) to (8,10)
# then we should have to create two new array with the values present inside them
# where one arrays contains the x-axis values 
# where the other one contains of y-axis values 
# Below is the example for the above statements 
# 
# import matplotlib.pyplot as plt 
# import numpy as np
# X_points = np . array ([1,8])
# Y_points = np . array ([3,10])
# plt . plot ( X_Points , Y_Points )         ///          if you need that line inbetween the points just use this line plt.plot(X_Points,Y_Points,'o')
# plt . show ()
# 
#
#
# If you want to plot multiple lines just prefer the numbers you needed to plot in the graph
# X_axis_points=( [ number1 , number2 , number3 , number4 , number5 ] )
# Y_axis_points=( [ number6 , number7 , number8 , number9 , numner10 ] )
#
#
# Let's move on to markers just learn the most commonly used function not every functions related to that particular topics , just like an bird spectacular eyesight towards the bottom line where most important things are birds prey 
# plt.plot ( Y_Points , marker ='o', ms=20 , mfc ='r' ,mec='b') 
# marker = 'o' <----  denotes the x-point and y-point meeting place where we can denote them as 'o' the 'o' will be shown in the plot 
# ms = 20      <----  denotes the size of the marker
# mfc = 'r'    <----  Marker face color
# mec = 'b'    <----  Marker border color 
#
#
# Now moving to the line, the characteristics of line can be said as size, colour, structure ect 
# plt.plot ( X_Points , Y_Points , color='r' , linewidth = 1  )   <-- This are for the line characteristics 
# plt.plot ( X_Points , Y_Points , color='r' , linewidth = 1 , marker ='o' , ms = 20 , mfc = 'r' , mec = 'b' )  <-- This line shows the combined of both the marker and line modifying changes on the plot than the default ones 
# 
# 
# Moving on to multiple lines 
# You can plot many number of lines on the plot by using the plot function where each lines will be stacked over one upon them 
# plt.plot ( X_Points )
# plt.plot ( Y_Points )
#
# Now moving on the next example, take 4 arrays with the name of x1, y1, x2, y2 
# where x1 and y1 creates a seperate line and x2 and y2 creates a seperate line and the both overlap on each other 
# x1=np.array([0,1,2,3])
# y1=np.array([3,8,1,10])
# x2=np.array([0,1,2,3])
# y2=np.array([6,2,7,11])
# plt.plot(x1,y1,x2,y2,color='r' , linewidth = 1 , marker ='o' , ms = 20 , mfc = 'r' , mec = 'b' )  
#                                        if you use plt.plot(x1,y1)   this will create one chart 
#                                                   plt.plot(x2,y2)   and then this will create another chart 
# plt.title("Title 1")
# plt.xlabel("X Label Title")
# plt.ylabel("Y Label Title")
#
# Grid --> Grid function is used to overlay the lines to the x-axis or y-axis or both 
# plt.grid(axix='x',axis='y', color='r' , linewidth = 1 ,)
#
#
# Display multiple sub plots, with the usage of sub plots we can able to draw multiple plots in one figure 
# A = np . array ([0,1,2,3])
# B = np . array ([3,8,1,10])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# A1= np .array([0,1,2,3])
# A2= np .array([10,20,30,40])
# plt.subplot(1,2,2)
# plt.plot(A1,A2)
# plt.show()
#













