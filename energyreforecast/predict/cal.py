import importlib
import numpy as np
import matplotlib.pyplot as plt
from .models import * 

def linear(x, y):    
    # number of observations/points
    n = np.size(x)
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="b",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color="y")

    # putting labels
    plt.xlabel('Production (Ton)')
    plt.ylabel('Energy (MWh)')

    # function to show plot
    plt.show()


def main():
    # observations / data
    #  x = np.array([4909, 4292, 4718, 4531, 5363, 5663, 5562, 5731, 5333, 4939])
    #  y = np.array([2271.25, 2038.14, 2301.18, 2222.81, 2593.91,2626.42, 2610.08, 2651.41, 2433.58, 2279.78])
    daily.objects.all().filter(name_zone='z').values('production','energy')
    x = np.array([production]),
    y = np.array([energy])
    # estimating coefficients
    
    print("Estimated coefficients: \n y = mx + b\n m = {} \
		\n b = {}".format(b[0], b[1]))

    # plotting regression line
    # plot_regression_line(x, y, b)
    return main()