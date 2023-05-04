import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mtcars = pd.read_csv('mtcars.csv')

# Filter the data by number of cylinders
mpg_4cyl = mtcars[mtcars['cyl'] == 4]['mpg'].mean()
mpg_6cyl = mtcars[mtcars['cyl'] == 6]['mpg'].mean()
mpg_8cyl = mtcars[mtcars['cyl'] == 8]['mpg'].mean()

# Creating MPG/cyl bar plot
plt.figure()
sns.barplot(x=['4 cyl', '6 cyl', '8 cyl'], y=[mpg_4cyl, mpg_6cyl, mpg_8cyl])
plt.ylabel('Mean MPG')
plt.xlabel('(Higher is better)')
plt.title("MPG compared to number of cylinders")

# Filter the data by number of cylinders
wt_4cyl = mtcars[mtcars['cyl'] == 4]['wt']
wt_6cyl = mtcars[mtcars['cyl'] == 6]['wt']
wt_8cyl = mtcars[mtcars['cyl'] == 8]['wt']

# Creating drat/cyl box plot
plt.figure()
plt.boxplot([wt_4cyl, wt_6cyl, wt_8cyl], labels=['4 cyl', '6 cyl', '8 cyl'])
plt.ylabel('Weight ratio')
plt.title('Weight ratio compared to number of cylinders')

# Filter the data by transmission type
mpg_auto = mtcars[mtcars['am'] == 0]['mpg'].mean()
mpg_manual = mtcars[mtcars['am'] == 1]['mpg'].mean()

# Creating MPG/transmission bar plot
plt.figure()
sns.barplot(x=['Automatic', 'Manual'], y=[mpg_auto, mpg_manual])
plt.ylabel('Mean MPG')
plt.xlabel('(Higher is better)')
plt.title("MPG compared to the type of transmission")

# Filter the data by transmission type
vs_auto = mtcars[mtcars['am'] == 0]['vs'].mean()
vs_manual = mtcars[mtcars['am'] == 1]['vs'].mean()

# Creating vs/transmission scatter plot
plt.figure()
plt.scatter(mtcars.qsec, mtcars.hp, c=mtcars.am, cmap='bwr')
plt.xlabel('Time per 1/4 mile')
plt.ylabel('Strength (hp)')

# Show the plot
plt.show()
