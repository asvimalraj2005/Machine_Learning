# Linear Regression
# Regression is used to find the relation ship between two variable or multiple variables 
# Linear regression is used to find the relation ship or predict the future events 
# 
# LR uses the relationship between the data-points to draw a straight line through all the points 
# Below is an example for linear regression
# 
# Scatterplot shows the plot on the users screen 
#
#
# import numpy as np                                                      <-- Importing numpy as np 
# import matplotlib.pyplot as plt                                         <-- Importing matplotlib as plt
#   
# Sample data                                                             <-- Creating a sample data
# x = np.array([5, 6, 7, 8, 9, 10, 11, 5, 11, 12, 9, 6])    
# y = np.array([86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])       
#   
# Scatter plot                                                            <-- By using scatterplot we are plotting the x,y points on the plot 
# plt.scatter(x, y, color="blue", label="Data Points")                    <-- Labelling 
# plt.xlabel('x')                                                         <-- Labelling the x axis
# plt.ylabel('y')                                                         <-- Labelling the y axis 
# plt.title('Scatter Plot of x vs y')                                     <-- Title 
#
# Linear Regression Coefficient Estimation
# def estimate_coef(x, y):                                                <-- Passing the arguments to this extimate_coef parameter 
#   n = np.size(x)                                                        <-- Getting the total length of x and storing it to on n 
#
#    # Mean of x and y
#    m_x = np.mean(x)                                                     <-- By using the mean function we are calculating the mean of x array 
#    m_y = np.mean(y)                                                     <-- By using the mean function we are calculating the mean of y array 
#
#    # Calculating cross-deviation and deviation about x
#    SS_xy = np.sum(y * x) - n * m_y * m_x                                <-- Calculating the cross-deviation for x 
#    SS_xx = np.sum(x * x) - n * m_x * m_x                                <-- Calculating the cross-deviation for y 
#
#    # Regression coefficients                                            <-- By using the formula SS_xy/SS_xx we are calculating the regression coefficients 
#    b_1 = SS_xy / SS_xx        
#    b_0 = m_y - b_1 * m_x                                                      
#
#    return (b_0, b_1)                                                    <-- Returning the b_0 and b_1 
#
# Estimate coefficients
# b_0, b_1 = estimate_coef(x, y)                                           <-- Passing the values here as the arguments 
#
# Plot regression line
# regression_line = b_0 + b_1 * x
# plt.plot(x, regression_line, color="red", label=f"Regression Line: y = {b_0:.2f} + {b_1:.2f}x")
#
# plt.legend()
# plt.show()
