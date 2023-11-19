# TODO find out if you have to draw plots as the task says (last part of the code as an example)
#  or is it enough to only print out the solutions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ucitavanje ociscenih podataka
df = pd.read_csv(Path('LV4/cars_processed.csv'))
df_sorted = df.sort_values('selling_price')

print("\n")
print(df.info())

print("Cheapest car: \n")
print(df_sorted[['name', 'selling_price']].head(1))

print("\nPriciest car: \n")
print(df_sorted[['name', 'selling_price']].tail(1))

print("\nCount of cars made in 2012:\n")
print(df[(df.year == 2012)].count()[['year']])

df_sorted = df.sort_values('km_driven')
print("\nCar with the most distance traveled: \n")
print(df_sorted[['name', 'km_driven']].tail(1))

print("\nCar with the least distance traveled: \n")
print(df_sorted[['name', 'km_driven']].head(1))

print("\nMost common number of seats:\n")
seat_counts = df['seats'].value_counts()
most_common_seats = seat_counts.idxmax()
print(most_common_seats)

print("\nAverage traveled km depending on fuel type:\n")
average_km_diesel = round(df[df['fuel'] == 'Diesel']['km_driven'].mean(), 2)
average_km_petrol = round(df[df['fuel'] == 'Petrol']['km_driven'].mean(), 2)
print("Diesel: ", average_km_diesel)
print("Petrol: ", average_km_petrol)


# Count of cars made in each year
year_counts = df['year'].value_counts().sort_index()

# Count of cars made in each year
year_counts = df['year'].value_counts().sort_index()

# Extract last two digits of year for x-axis labels
x_labels = year_counts.index.astype(str).str[-2:]

# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=x_labels, y=year_counts.values)
plt.xlabel('Year')
plt.ylabel('Count of Cars')
plt.title('Number of Cars by Year')
plt.show()
