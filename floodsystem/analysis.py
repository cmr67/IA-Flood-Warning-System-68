import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    
    p = 3 # This is for the number of degrees for the ploynomial later
    x = matplotlib.dates.date2num(dates) # Dates as function of their argument
    ploy, d0 = polyfit(dates,levels, p) # Polynomial for p degrees
    d0 = x[0] # The shift of the date (time) axis at the initial/first date

    p_coeff = np.polyfit(x - d0, levels, p) # Using shifted x values to find coefficient for best fit

    poly = np.poly1d(p_coeff) # Converting polynomial into coefficients to be evaluated - polynomial function

    return poly, d0 # Return results