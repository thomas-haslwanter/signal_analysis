""" Effects Linear and non-linear filters on data with extreme outliers """

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Create the data
x = np.zeros(20)
x[10:] = 1

# Add some noise-spikes
x[[5,15]] = 3

# Median filter the signal
x_med = signal.medfilt(x, 3)

# Average filtered data
b = np.ones(3)/3
x_filt = signal.lfilter(b, 1, x)

# Plot the data
plt.plot(x, 'o', linestyle='dotted', label='rawdata')
plt.plot(x_filt[1:], label='average')
plt.plot(x_med, label='median')

plt.xlim([0, 19])
plt.xticks(np.arange(0,20,2))
plt.legend()

ax = plt.gca()
ax.margins(x=0, y=0.02)

# Save and show the image
out_file = 'MedianFilter.jpg'
plt.savefig(out_file, dpi=200, quality=90)
print(f'Image saved to {out_file}')

plt.show()
