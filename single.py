# NumPy is a python library for scientific computing 
import numpy as np 
# matplotlib is a 2D plotting library
import matplotlib.pylab as plt 

# Creating the function estimate_coef 
def estimate_coef(x, y):
    #number of observations/points
    # variable n is equal to the  size of array x which is 10
    n = np.size(x) 

    #mean of x and y vector
    # This is to get an average of these set of values.
    m_x, m_y = np.mean(x), np.mean(y)

    #calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    #calulating regression coefficients
    # Represent y interpect and the slope 
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)

def plot_regression_line(x, y,b):

    #plotting the actual points as scatter plot
    # Changes the color of the plots with the variable color and the shape, you can make them any shape with the variable marker
    #size is the variable s, so you can change the size of the plots on your graph
    plt.scatter(x, y, color = "w", marker = "o", s = 15)

    # predicted response vector 
    y_pred = b[0] + b[1]*x 

    # plotting the regression line
    #Change the color of the regression line with the variable color
    # r = red, w = white, b = blue etc.
    plt.plot(x, y_pred, color = "r")

    # putting labels 
    plt.xlabel('Size(feet)^2')
    plt.ylabel('Price($1000)')

    # function to show plot
    plt.show()

# Main function 
def main():
    #obervations
    #Made up a random dataset that relates to the housing prices example we worked on in the tuesday classes
    x = np.array([8000,7660,7210,7000,6648,6100,5800,5710,5480,5270,5000,4800,4610,4300,4000,3642,3444,3322,3104,3000,2800,2600,2420,2104,2000,1800,1622,1534,1416,1380,1300,1100,1050,1000,980,940,900,852]) 
    y = np.array([2440,2400,2360,2320,2280,2100,2060,1800,1600,1700,1510,1300,1200,1000,1120,1030,890,760,740,680,660,580,540,440,410,390,600,320,230,220,500,290,300,14,300,115,5,20])

    #estimating coefficients
    b = estimate_coef(x,y)
    print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0],b[1]))
    
    # Calling plot_regression_line function 
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
