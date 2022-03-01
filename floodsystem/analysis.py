import numpy as np
import matplotlib
def polyfit(dates, levels, p):
    
#    p = 4 # This is for the number of degrees for the ploynomial later
    x = matplotlib.dates.date2num(dates) # Dates as function of their argument
    d0 = 1
    #poly, d0 = polyfit(dates, levels, p) # Polynomial for p degrees
    times_shift = x - x[-d0] # The shift of the date (time) axis at the initial/first date
    p_coeff = np.polyfit(times_shift, levels, p) # Using shifted x values to find coefficient for best fit
    poly = np.poly1d(p_coeff) # Converting polynomial into coefficients to be evaluated - polynomial function

    return poly, d0 # Return results


dates =[1,2,3,4,5]
levels = [1,2,3,4,5]
p =4
polyfit(dates,levels,p)