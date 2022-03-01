import numpy as np
import matplotlib
from .utils import sorted_by_key
from .datafetcher import fetch_measure_levels
import datetime

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


def flood_warning(stations):
    x = []
    dt = 1
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 0.5:
                dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
                if len(levels) > 0:    
                    d_level = levels[len(levels)-1] - levels[0]
                    tuple = (station.name, d_level)
                    x.append(tuple)
    x_sort = sorted_by_key(x, 1)
    low = x_sort [int(len(x_sort)*0.3) : ]    
    moderate = x_sort [int(len(x_sort)*0.3) :int(len(x_sort)*0.6)]
    high = x_sort[int(len(x_sort)*0.6) : int(len(x_sort)*0.9)]
    severe = x [int(len(x_sort)*0.9):]

    return low, moderate, high, severe