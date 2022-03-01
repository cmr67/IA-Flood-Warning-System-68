import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit
from .stationdata import build_station_list
import numpy as np

def plot_water_levels(station, dates, levels):
    stations=build_station_list()
    # The high and low typical ranges
    low_levels = station.typical_range[0]
    high_level = station.typical_range[1]

    # Plotting the current data and the typical high and low ranges
    plt.plot(dates, levels, label = "Current startion data")
    plt.plot(dates, low_levels, label = "Low Typical Water Level")
    plt.plot(dates, high_level, label = "High Typical Water Level")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    for station in stations:
        plt.title("Water Level for {}" .format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

    return

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates, levels, p)
    x = np.linespace(0, x.dates[d0:-1], len(dates))

    plt.plot(dates, x)
    plt.plot(dates, poly)
    plt.legend()
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Level Data and best-fit polynomial for" .format(station.measure_id))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
