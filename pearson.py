import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import scipy.fftpack

fig = plt.figure(figsize=(20,8),dpi = 80)

y = pd.read_csv('./Data/y4.csv', sep=',',header=None)
x = pd.read_csv('./Data/x4.csv', sep=',',header=None)
r,p = stats.pearsonr(x[1].to_list(),y[1].to_list())
print(f"Scipy computed Pearson r: {r} and p-value: {p}")

axis = y[0].to_list()
#print(axis)
plt.plot(axis,x[1].to_list(),color='blue')
plt.plot(axis,y[1].to_list(),color='red')


plt.title(f"Overall Pearson r = {np.round(r,2)}", fontsize= 16, fontweight = 'bold')
plt.ylabel('Value', fontsize = 16, fontweight = 'bold')
