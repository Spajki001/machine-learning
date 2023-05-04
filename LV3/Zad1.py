import pandas as pd

pd.set_option('display.max_columns', None)
mtcars = pd.read_csv('mtcars.csv')
mpg_mtcars = mtcars.sort_values(by='mpg', ascending=[False])

# 5 cars with the most mpg
print("5 cars with the least mpg:")
print(mpg_mtcars[['car', 'mpg']].tail(5))

# 3 cars with 8 cylinders and least mpg
print("\n3 cars with 8 cylinders and least mpg:")
print(mpg_mtcars[(mpg_mtcars.cyl == 8)][['car', 'mpg', 'cyl']].tail(3))

# Mean mpg in cars with 6 cylinders
print("\nMean mpg in cars with 6 cylinders:")
print(round(mtcars[(mtcars.cyl == 6)][['mpg']].mean(), 2))

# Mean mpg in cars with 4 cylinders and weight between 2000 and 2200 lbs
print("\nMean mpg in cars with 4 cylinders and weight between 2000 and 2200 lbs:")
print(mtcars[(mtcars.cyl == 4) & ((mtcars.wt * 1000) > 2000) & ((mtcars.wt * 1000) < 2200)][['mpg']].mean())

# Amount of cars with and without automatic transmission
print("\nAmount of cars with manual transmission:")
print(mtcars[(mtcars.am == 1)].count()[['am']])
print("\nAmount of cars with automatic transmission:")
print(mtcars[(mtcars.am == 0)].count()[['am']])

# Amount of cars with automatic transmission and over 100 hp
print("\nAmount of cars with automatic transmission and over 100 hp:")
print(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)].count()[['hp']])

# Calculate all weight info to kg for each car
print("\nTable with every weight in kg:")
mtcars_kg = mtcars.copy()
mtcars_kg['wt'] = round((mtcars_kg['wt'] * 1000) * 0.45359237, 2)
print(mtcars_kg[['car', 'wt']])
