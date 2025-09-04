# Import necessary libraries
import plotly.express as px
import pandas as pd
import plotly.io as pio

# Set default renderer to open plots in browser
pio.renderers.default = 'browser'

# Load dataset
df = pd.read_csv("tourism_data.csv")

# Line chart – Monthly Tourist Arrivals
fig = px.line(df, x='Month', y='Tourist_Arrivals', title='Monthly Tourist Arrivals')
fig.show()

# ================= Inferences & Visualizations =================

# Bar chart – Tourist Arrivals by Country
# Useful for comparing which countries contribute more tourists
df = pd.read_csv("tourism_data.csv")
fig = px.bar(df, x='Country', y='Tourist_Arrivals', title='Monthly Tourist Arrivals')
fig.show()

# Scatter plot – Hotel Bookings vs. Average Travel Cost
# Helps analyze relationship between cost and booking trends
df = pd.read_csv("tourism_data.csv")
fig = px.scatter(df, x='Average_Travel_Cost', y='Hotel_Bookings', title='Hotel Bookings vs. Travel Cost')
fig.show()

# Histogram – Distribution of Hotel Prices
fig = px.histogram(df, x='Hotel_Price', title='Distribution of Hotel Prices')
fig.show()

# Violin plot – Seasonal Variation in Travel Cost
# Shows spread of costs across different travel seasons
fig = px.violin(df, x='Season', y='Average_Travel_Cost',box=True, title='Seasonal Variation in Travel Cost')
fig.show()

# Timeline chart – Tourism Itinerary (activities over start and end dates)
fig = px.timeline(df, x_start='Start_Date', x_end='End_Date',y='Activity', title='Tourism Itinerary')
fig.show()

# 3D Scatter – Relationship between Travel Cost, Hotel Rating & Bookings
fig= px.scatter_3d(df, x='Average_Travel_Cost',y='Hotel_Rating',z='Hotel_Bookings',
                   title= '3D Analysis of Travel Cost, Ratings & Bookings', color='Hotel_Rating')
fig.show()