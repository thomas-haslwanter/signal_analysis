""" Show the effect of an FIR- and an IIR-filter on an impulse """

# author:   Thomas Haslwanter
# date:	    April-2020

# Import the standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# additional packages
# Import formatting commands if directory "Utilities" is available
import os
import sys
sys.path.append(os.path.join('..', 'Code_Quantlets', 'Utilities'))
try:
    from SAP_mystyle import set_fonts, show_data 
except:
    print('I could not load SAP_mystyle')

# Generate the impulse, and the time-axis
xx = np.zeros(20)
xx[5] = 1
tt = np.arange(20)

# Put the results into a Python-dictionary
data = {}
data['before'] = xx
data['after_fir'] = signal.lfilter(np.ones(5)/5, 1, xx)
data['after_iir'] = signal.lfilter([1], [1, -0.5], xx)

# Show the results
plt.plot(tt, data['before'], 'o', label='input', lw=2)
plt.plot(tt, data['after_fir'], 'x-', label='FIR-filtered', lw=2)
plt.plot(tt, data['after_iir'], '.:', label='IIR-filtered', lw=2)
plt.xlabel('Timesteps')
plt.ylabel('Signal')

plt.legend()
plt.xlim([0, 20])
plt.xticks(np.arange(0, 20, 2))

out_file = 'FIRvsIIR.jpg'

show_data(out_file)