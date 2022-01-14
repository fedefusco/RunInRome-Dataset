import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

'''
  Plot of the points on the map of Rome
'''

max_latitude, min_latitude = 41.9197, 41.8672
min_longitude, max_longitude  = 12.4415,  12.5328

box = (min_longitude, max_longitude, min_latitude, max_latitude)
# Coordinates corresponding to the boundaries of Rome.png, as in https://www.openstreetmap.org/


# Import the data as pd dataframe
df = pd.read_csv('RunInRome.csv', names = ['latitude', 'longitude']) 

# Import of the map and plot of the points
rome_map = plt.imread('Rome.png')
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
ax.scatter(df.longitude, df.latitude, c='b', s=1)
ax.set_title('Tracking activity in Rome')
ax.imshow(rome_map, extent = box, aspect= 'equal')

plt.show()




