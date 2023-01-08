#!/usr/bin/env python3

# Import required packages
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm

CSV_FILENAME = 'metrics_dynamic_scheduler_GreedyLB_memory.csv'

timestamp, node1, node2, node3 = np.loadtxt(CSV_FILENAME, unpack=True, delimiter=',', skiprows=1)

def to_relative_time(n):
  return n - timestamp[0]

relative_time = list(map(to_relative_time, timestamp))

print(relative_time)

# Create figure and add axes object
#fig = plt.figure()
#ax = fig.add_axes([0, 0, 1, 1])
# Plot and show our data
plt.plot(relative_time, node1)
#ax.plot(timestamp, node2)
#plt.show()

# Save figure
plt.savefig('Final_Plot.png', dpi=300, transparent=False, bbox_inches='tight')
