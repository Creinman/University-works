import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.12, 5.12, 0.1)
y = 10 + x**2 - 10*np.cos(2*np.pi*x)
fig, ax = plt.subplots()
ax.plot(x, y)  
lgnd = ax.legend(['y'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('green')
plt.show()
