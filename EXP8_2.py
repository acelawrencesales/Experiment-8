import pandas as pd

cars = pd.read_csv('cars.csv')

#a
a = cars.loc[1:10:2]
print(a)

#b
b = cars[cars['Model'] == 'Mazda RX4']
print(b)

#c
#to identify the index of Camaro Z28
cars[cars['Model'] == 'Camaro Z28']
c = cars.loc[[23], ['Model', 'cyl']]
print(c)

#d
#to identify the index of Mazda RX4 Wag, Ford Pantera L, and Honda Civic
cars[cars['Model'] == 'Mazda RX4 Wag']
cars[cars['Model'] == 'Ford Pantera L']
cars[cars['Model'] == 'Honda Civic']

d = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
print(d)