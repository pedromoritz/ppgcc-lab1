#!/usr/bin/env python3

import os
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pylab import cm
import sys
from collections.abc import Iterable

def save_graphic(timestamp, data1, data2, data3, data4, xlabel, ylim, ylabel, final_filename, migrations):
  plt.xlabel(xlabel)
  plt.ylim(0, ylim)
  plt.ylabel(ylabel)
  plt.plot(timestamp, data1, label='node 1', linewidth='2')
  plt.plot(timestamp, data2, label='node 2', linewidth='2')
  plt.plot(timestamp, data3, label='node 3', linewidth='2')
  plt.plot(timestamp, data4, label='node 4', linewidth='2')
  if isinstance(migrations, Iterable):
    for migration in migrations:
      plt.axvline(x = migration, color = 'red', linewidth='0.7', linestyle='dashed')
  plt.legend(loc="upper left")
  print("Generating " + final_filename)
  #plt.axes().yaxis.grid()
  plt.savefig(final_filename, dpi=400, transparent=False, bbox_inches='tight')
  plt.legend(loc="upper left")
  plt.close()
  plt.cla()
  plt.clf()

for path in Path("results/").glob("metrics_*.csv"):
  FILE_NAME, FILE_EXTENSION = os.path.splitext(path)
  print("Reading " + str(path))
  timestamp, node1_pod_amount, node1_memory, node1_cpu, node2_pod_amount, node2_memory, node2_cpu, node3_pod_amount, node3_memory, node3_cpu, node4_pod_amount, node4_memory, node4_cpu = np.loadtxt(FILE_NAME + '.csv', unpack=True, delimiter=',', skiprows=1)

  migrations = []

  if 'kube-scheduler' in FILE_NAME:
    # generating memory graphics
    data1 = list(map(lambda n: n/1024, node1_memory))
    data2 = list(map(lambda n: n/1024, node2_memory))
    data3 = list(map(lambda n: n/1024, node3_memory))
    data4 = list(map(lambda n: n/1024, node4_memory))
    xlabel = 'time (s)'
    ylim = 2048
    ylabel = 'memory (MB)'
    final_filename = FILE_NAME + '_memory.png'
    save_graphic(timestamp, data1, data2, data3, data4, xlabel, ylim, ylabel, final_filename, migrations)
    # generating cpu graphics
    data1 = list(map(lambda n: n/1000000, node1_cpu))
    data2 = list(map(lambda n: n/1000000, node2_cpu))
    data3 = list(map(lambda n: n/1000000, node3_cpu))
    data4 = list(map(lambda n: n/1000000, node4_cpu))
    xlabel = 'time (s)'
    ylim = 2000
    ylabel = 'CPU (millicpu)'
    final_filename = FILE_NAME + '_cpu.png'
    save_graphic(timestamp, data1, data2, data3, data4, xlabel, ylim, ylabel, final_filename, migrations)
  elif 'kse' in FILE_NAME:
    if 'memory' in FILE_NAME:
      # generating memory graphics
      data1 = list(map(lambda n: n/1024, node1_memory))
      data2 = list(map(lambda n: n/1024, node2_memory))
      data3 = list(map(lambda n: n/1024, node3_memory))
      data4 = list(map(lambda n: n/1024, node4_memory))
      xlabel = 'time (s)'
      ylim = 2048
      ylabel = 'memory (MB)'
      final_filename = FILE_NAME + '.png'
      MIGRATIONS_FILE_NAME = FILE_NAME.replace('metrics', 'migrations')
      migrations = np.loadtxt(MIGRATIONS_FILE_NAME + '.csv', unpack=True, delimiter=',', skiprows=0, usecols=[0])
      save_graphic(timestamp, data1, data2, data3, data4, xlabel, ylim, ylabel, final_filename, migrations)
    elif 'cpu' in FILE_NAME:
      # generating cpu graphics
      data1 = list(map(lambda n: n/1000000, node1_cpu))
      data2 = list(map(lambda n: n/1000000, node2_cpu))
      data3 = list(map(lambda n: n/1000000, node3_cpu))
      data4 = list(map(lambda n: n/1000000, node4_cpu))
      xlabel = 'time (s)'
      ylim = 2000
      ylabel = 'CPU (millicpu)'
      final_filename = FILE_NAME + '.png'
      MIGRATIONS_FILE_NAME = FILE_NAME.replace('metrics', 'migrations')
      migrations = np.loadtxt(MIGRATIONS_FILE_NAME + '.csv', unpack=True, delimiter=',', skiprows=0, usecols=[0])
      save_graphic(timestamp, data1, data2, data3, data4, xlabel, ylim, ylabel, final_filename, migrations)
