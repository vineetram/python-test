#Importing Libraries
import pandas as pd
#Importing the dataset
from nsepy import get_history
from datetime import date
data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2016,1,31))

#Part 1
#Creatng 4,16,....,52 week moving average(closing price) for each stock and index.
v =  data.iloc[:, 7].values
def Average(v): 
    return sum(v) / len(v) 
average = Average(v) 

#Creating the following dummy time series
#3.1 Volume shocks
#If volume traded is 10% higher/lower than previous day
c = data.iloc[:, 10].values
for i in range(0,268):
    if c[i]*(10/100) > c[i-1]:
        print("Volume Traded is higher than 10%")
    else:
        c[i]*(10/100) < c[i-1]
        pd.get_dummies(c, prefix=['col1', 'col2'])

#3.2 Price shocks
#If closing price at T vs T+1 has a difference > 2%
for i in range(0,267):
    if v[i]-v[i+1] > 0.02:
       pd.get_dummies(v, prefix=['col1', 'col2'])
    else:
        print(" closing price at T vs T+1 has a difference < 2%")
    
#3.4 Pricing shock without volume shock    
#Pricing shock without volume shock
for i in range(0,268):
     if c[i]*(10/100) < c[i-1]:
        pd.get_dummies(c, prefix=['col1', 'col2'])
     else:
        v[i]-v[i+1] > 0.02
        pd.get_dummies(v, prefix=['col1', 'col2'])

#Part 2 (data visualization ):
#IMPORTING BOKEH
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool

#Define the output file path
output_file("stock.html")

#Create the figure object
f=figure()

#Style the tools
f.tools = [PanTool(),ResetTool()]
hover = HoverTool(tooltips=[("Close","@close"), ("Volume","@volume")])
f.add_tools(hover)
f.toolbar_location = 'above'
f.toolbar.logo = None

#Style the plot area
f.plot_width = 1100
f.plot_height = 650
f.background_fill_color = "olive"
f.background_fill_alpha = 0.3         

#Style the title
f.title.text = "Assignment"
f.title.text_color = "olive"
f.title.text_font = "Agency FB"
f.title.text_font_size = "25px"
f.title.align = "center"        

#Style the axes
f.xaxis.minor_tick_line_color = "blue"
f.yaxis.major_label_orientation = "vertical"
f.xaxis.visible = True
f.xaxis.minor_tick_in = -6
f.xaxis.axis_label = "Close"
f.yaxis.axis_label = "Volumes"
f.axis.axis_label_text_color = "blue"
f.axis.major_label_text_color = "red"

#Axes geometry
f.x_range = Range1d(start=0, end=10)
f.y_range = Range1d(start=0, end=5)
f.xaxis.bounds = (2,6)
f.xaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.num_minor_ticks = 10

#Style the grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha = 0.6
f.grid.grid_line_dash = [5,3]

#Style the legend
f.legend.location = (575,555)
f.legend.location = 'top_left'
f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'times'

#Save and show the figure
show(f)