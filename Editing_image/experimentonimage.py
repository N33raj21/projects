import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 5))
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
ax.plot(t, s, lw=3)

# Annotate with text
ax.annotate('Your text here', xy=(0.5, -1), xycoords='data', xytext=(-80, -60),
            textcoords='offset points', arrowprops=dict(arrowstyle="->"))

# Save or display the plot
plt.savefig('annotated_plot.png')
plt.show()
