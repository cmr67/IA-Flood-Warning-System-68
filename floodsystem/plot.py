import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    # The high and low typical ranges
    low_levels = station.typical_range[0]
    high_level = station.typical_rnage[1]

    # Plotting the current data and the typical high and low ranges
    plt.plot(dates, levels, label = "Current startion data")
    plt.plot(dates, low_levels, label = "Low Typical Water Level")
    plt.plot(dates, high_level, label = "High Typical Water Level")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Level for" .format(station))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()

    return