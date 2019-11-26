import pandas as pd

cars = pd.read_csv('cars.csv')

ffive = cars.head()
lfive = cars.tail()

print(ffive, lfive)