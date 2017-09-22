# Rixing Xu
#
# This program uses the Monte Carlo method to calculate pi (using 1/4 area of square to get to area of quarter circle), area of a circle is pi r^2 and area of a square is (2r)^2. Then plotted the distribution of the calculated pi values.
#
# This program also calculates the quality of the calculated pi values with increasing points

import random
import math
import numpy as np
import matplotlib.pyplot as plt

datax = []
datay = []

count = 0 # this will keep track of the number of points found in that quarter circle
datac = [] # this will hold the number of calculated Pi values
piValues = 500 # how many pi values we will calculate
totalPoints = 1000 # how many points we set to be found in that quarter of the square
dataPi = [] 

# this simulates points for square (x,y) between 0 and 1
for i in range(1000):
    datax.append(random.random())
    datay.append(random.random())

# circle function

# This function finds if point is in circle by using a quarter of a circle (upper right quadrant) and takes in a 
def calculatePi(pValue):
    for k in range(pValue):
        j = 0
        count = 0
        while (j < circlePoints):
            x = (random.random()*(0.5)) + (0.5) # taking a random point in the upper right quadrant of circle
            circleEq = (0.5) + math.sqrt(0.25-((x - (0.5))**2)) # the circle equation for a circle of center (0.5, 0.5) and radius 1
            y = (random.random()*(0.5)) + (0.5)
    
            if (y <= circleEq):
                count += 1
            j += 1  
        
        frac = (count)/float(circlePoints)
        pi = frac * 4
        datac.append(pi)
        
    return datac

plt.hist(calculatePi(piValues), bins = 20, normed = True)
plt.xlabel("Value of Pi")
plt.ylabel("Count")
plt.title("Calculating Pi")
        
plt.show()

uncertainty = []
xValues = []
# Then we want to plot the uncertainty vs the number of random points
for l in range(10):
    dataPi = calculatePi(piValues + (10*l))
    xValues.append(piValues + (10*l))
    mean = np.mean(dataPi)
    std = np.std(dataPi)
    uncertainty.append((abs((math.pi - mean))))
    #print(uncertainty)
    
plt.plot(xValues, uncertainty)
plt.xlabel("Number of random points used")
plt.ylabel("Uncertainty of Pi")
plt.title("Uncertainty of Pi vs Number of Random Points")
plt.show()




        
