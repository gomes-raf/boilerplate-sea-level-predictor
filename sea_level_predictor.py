import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    previsao_2050 = pd.Series(range(1880, 2051))
    
    slope, intercept, r, p, se = linregress(x, y)
    plt.plot(previsao_2050, intercept + slope * previsao_2050, 'r', label='Fitted line')

    # Create second line of best fit
    x_2000 = df[df['Year'] >= 2000]['Year']
    y_2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']

    previsao_2000 = pd.Series(range(2000, 2051))
    
    slope_2000, intercept_2000, r_2000, p_2000, se_2000 = linregress(x_2000, y_2000)
    plt.plot(previsao_2000, intercept_2000 + slope_2000 * previsao_2000, 'b', label='Fitted line 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()