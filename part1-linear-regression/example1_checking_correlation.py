import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# gets the data and sets x and y values
data = pd.read_csv("part1-linear-regression/chirping_data.csv")
x = data["Temp"]
y = data["Chirps"]

# sets the size of the graph
plt.figure(figsize=(6,4))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("blood pressure")
plt.ylabel("age")
plt.title("Blood pressure by age")

# prints the correlation coefficient
print(f"Correlation between age and blood pressure: {x.corr(y)}")

# show the plot
plt.show()