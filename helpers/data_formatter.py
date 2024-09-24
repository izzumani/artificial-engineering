import numpy
from matplotlib.ticker import Formatter
# Define a class for formatting
class DataFormatter(Formatter):
    def __init__ (self, dates, date_format='%Y-%m-%d'):
        self.dates = dates
        self.date_format = date_format
    # Extract the value at time t at position ‘position’
    def call (self, t, position=0):
        index = int(round(t))
        if index >= len(self.dates) or index < 0:
            return ''
        return self.dates[index].strftime(self.date_format)