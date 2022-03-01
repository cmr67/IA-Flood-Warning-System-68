import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    
    low_level = station.typical_range[0]
    high_level = station.typical_range[1]

    plt.plot(dates, levels) # Plot for the dates and levels
    # Add axis labels, rotate date labels and add plot title
    plt.plot(dates, [low_level]*len(dates), label = "Typical Low Range")
    plt.plot(dates, [high_level]*len(dates), label = "Typical High Range")
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Level for {}" .format(station.name))

    # Display plot
    plt.legend()
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates, levels, p)

    low_level = station.typical_range[0]
    high_level = station.typical_range[1]

    plt.plot(dates, poly(x - x[-d0]))
    plt.plot(dates, [low_level]*len(x), label = "Typical Low Range")
    plt.plot(dates, [high_level]*len(x), label = "Typical High Range")
    plt.legend()
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Level Data and best-fit polynomial for {}" .format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
