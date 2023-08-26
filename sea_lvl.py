import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv',index_col='Year')
    x=df.index
    y=df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig,axes =plt.subplots()
    plt.scatter(x=x, y=y)

    # Create first line of best fit
    x_p=pd.Series([i for i in range(1880,2050)])
    y_p=linregress(x,y).slope*x_p + linregress(x,y).intercept
    plt.plot(x_p,y_p,'r--')

    # Create second line of best fit
    x2=df[df.index.values>=2000].index
    y2=df[df.index.values>=2000]['CSIRO Adjusted Sea Level']
    x_p2=pd.Series([i for i in range(2000,2050)])
    y_p2=linregress(x2,y2).slope*x_p2 + linregress(x2,y2).intercept
    plt.plot(x_p2,y_p2,'r')

    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level "Inches"')
    axes.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()