import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as mpatches

B='Are you measuring with or without the aid of blocks?'
L='What is the length of the bolt L in millimeters?'
D='What is the diameter of the bolt D in millimeters?'
P='What is the thread pitch P in millimeters'

# Make a list of columns
columns = [B,L,D,P]
colors = {'With blocks':'red','No blocks':'blue'}
dummy = pd.read_csv('Student_Bolt_Data.csv', usecols=columns)
df = dummy[dummy[B] == 'With blocks']
##Length

#Length
qlow_L= df[L].quantile(0.01)
qhi_L= df[L].quantile(0.99)
df_filteredL = df[(df[L] < 220) & (df[L] > 70)]

#Diameter
qlow= df[D].quantile(0.01)
qhi= df[D].quantile(0.99)
df_filteredD = df[(df[D] < 15) & (df[D] > 5)]

#Pitch
qlow= df[P].quantile(0.01)
qhi= df[P].quantile(0.99)
df_filteredP = df[(df[P] < 2.5) & (df[P] > qlow)]

#Renaming headers - cannot work with version it is only a temporary copy
correct_df = df_filteredL.copy()
correct_df.rename(columns={B: 'Blocks', L:'Length (mm)', D:'Diameter (mm)', P:'Pitch (mm)'}, inplace = True)
print(correct_df)

#Subplot length
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12,5), sharey = True)

df.reset_index().plot.scatter(x = 'index', y = L, c=df[B].map(colors), ax=ax0)
ax0.set_yticks(np.arange(0, 250, 10))
ax0.set_xlabel('Student no.')
ax0.set_ylabel('Length (mm)')
ax0.set_title('Bolt Length (Raw)')
ax0.tick_params(axis='both')

df_filteredL.reset_index().plot.scatter(x = 'index', y = L, c=df_filteredL[B].map(colors), ax=ax1)
ax1.set_xlabel('Student no.')
ax1.set_ylabel('Length (mm)')
ax1.set_title('Bolt Length (Cleaned)')
ax1.tick_params(axis='both')

red_patch = mpatches.Patch(color='red', label='With Blocks')
blue_patch = mpatches.Patch(color='blue', label='No Blocks')
plt.legend(handles=[red_patch, blue_patch])

#Diameter Subplot
fig, (ax2, ax3) = plt.subplots(1, 2, figsize=(12,5))

df.reset_index().plot.scatter(x = 'index', y = D, c=df[B].map(colors), ax=ax2)
ax2.set_yticks(np.arange(0, 100, 5))
ax2.set_xlabel('Student no.')
ax2.set_ylabel('Diameter (mm)')
ax2.set_title('Bolt Diamter (Raw)')
ax2.tick_params(axis='both')

df_filteredD.reset_index().plot.scatter(x = 'index', y = D, c=df_filteredD[B].map(colors), ax=ax3)
ax2.set_yticks(np.arange(0, 50, 5))
ax3.set_xlabel('Student no.')
ax3.set_ylabel('Diameter (mm)')
ax3.set_title('Bolt Diameter (Cleaned)')
ax3.tick_params(axis='both')

red_patch = mpatches.Patch(color='red', label='With Blocks')
blue_patch = mpatches.Patch(color='blue', label='No Blocks')
plt.legend(handles=[red_patch, blue_patch])

#Pitch Subplot
fig, (ax4, ax5) = plt.subplots(1, 2, figsize=(12,5),)

df.reset_index().plot.scatter(x = 'index', y = P, c=df[B].map(colors), ax=ax4)
ax4.set_yticks(np.arange(0, 40, 2))
ax4.set_xlabel('Student no.')
ax4.set_ylabel('Pitch (mm)')
ax4.set_title('Bolt Pitch (Raw)')
ax4.tick_params(axis='both')

df_filteredP.reset_index().plot.scatter(x = 'index', y = P, c=df_filteredP[B].map(colors), ax=ax5)
ax5.set_yticks(np.arange(0, 3, 0.2))
ax4.set_xlabel('Student no.')
ax5.set_ylabel('Pitch (mm)')
ax5.set_title('Bolt Pitch (Cleaned)')
ax5.tick_params(axis='both')

plt.tight_layout()
red_patch = mpatches.Patch(color='red', label='With Blocks')
blue_patch = mpatches.Patch(color='blue', label='No Blocks')
plt.legend(handles=[red_patch, blue_patch])

plt.tight_layout()

opt_binN = math.ceil(math.sqrt(len(df_filteredD[D]))+1)
fig, ax = plt.subplots(tight_layout=True)
ax.hist(df_filteredD[D], opt_binN)
ax.set_xticks(np.arange(0, 20, 1))
ax.set_xlabel('Diameter (mm)')
ax.set_ylabel('Frequency')
ax.set_title('Bolt Diameter Histogram')
ax.tick_params(axis='both')

opt_binN2 = math.ceil(math.sqrt(len(df_filteredL[L]))+1)
fig, ax = plt.subplots(tight_layout=True)
ax.set_xticks(np.arange(0, 250, 10))
ax.hist(df_filteredL[L], opt_binN2)
ax.set_xlabel('Length (mm)')
ax.set_ylabel('Frequency')
ax.set_title('Bolt Length Histogram')
ax.tick_params(axis='both')

opt_binN3 = math.ceil(math.sqrt(len(df_filteredP[P]))+1)
fig, ax = plt.subplots(tight_layout=True)
ax.set_xticks(np.arange(0, 50, 2))
ax.hist(df_filteredP[P], opt_binN3)
ax.set_xlabel('Pitch (mm)')
ax.set_ylabel('Frequency')
ax.set_title('Bolt Pitch Histogram')
ax.tick_params(axis='both')

plt.show()







