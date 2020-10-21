import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('User Identification From Walking Activity/5.csv',header=None)
data.columns = ['timestep','x','y','z']
print (data.head(5))

##Plotting
x_axis = data.timestep.values
y_axis = data.x.values
plt.plot(x_axis,y_axis)
plt.title('accelearation with time')
plt.xlabel('time')
plt.ylabel('acceleration')
plt.savefig('test.png')
