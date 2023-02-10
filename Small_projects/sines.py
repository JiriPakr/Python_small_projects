import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2*np.pi, 0.05)
x = np.cos(t)
plt.figure(figsize=(10,5))
plt.plot(t,x)