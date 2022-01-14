import smopy
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

'''
  Plot of the points on the map of Rome
'''

max_latitude, min_latitude = 41.9150, 41.8680
min_longitude, max_longitude  = 12.4549,  12.5352
box = (min_longitude, max_longitude, min_latitude, max_latitude)
# Coordinates corresponding to the boundaries of Rome.png, as in https://www.openstreetmap.org/


# Import the data as pd dataframe
df = pd.read_csv('RunInRome.csv', names = ['latitude', 'longitude']) 

# Import of the map and plot of the points
rome_map = plt.imread('Rome.png')
fig, ax = plt.subplots()
ax.scatter(df.longitude, df.latitude, c='b', s=5)
ax.set_title('Tracking activity in Rome')
ax.imshow(rome_map, extent = box, aspect= 'equal')

plt.show()



