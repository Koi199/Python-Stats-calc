import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import math

B='Are you measuring with or without the aid of blocks?'
L='What is the length of the bolt L in millimeters?'
D='What is the diameter of the bolt D in millimeters?'
P='What is the thread pitch P in millimeters'

# Make a list of columns
columns = [B,L,D,P]
colors = {'With blocks':'red','No blocks':'blue'}
df = pd.read_csv('Student_Bolt_Data.csv', usecols=columns)

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

df_filteredL1 = df[(df[L] < 225) & (df[L] > 175)]
df_filteredL2 = df[(df[L] < 175) & (df[L] > 125)]
df_filteredL3 = df[(df[L] < 125) & (df[L] > 75)]

df_filteredD1 = df[(df[D] < 14) & (df[D] > 11)]
df_filteredD2 = df[(df[D] < 11) & (df[D] > 9.5)]
df_filteredD3 = df[(df[D] < 9.5) & (df[D] > 8)]
df_filteredD4 = df[(df[D] < 8) & (df[D] > 4)]

df_sortedD1 = np.sort(df_filteredD1[D])
meanD1 = np.mean(df_sortedD1)
sdD1 = np.std(df_sortedD1)
modeD1 = df_filteredD1[D].mode
print(modeD1)

df_sortedD2 = np.sort(df_filteredD2[D])
meanD2 = np.mean(df_sortedD2)
sdD2 = np.std(df_sortedD2)
modeD2 = df_filteredD2[D].mode
print(modeD2)

df_sortedD3 = np.sort(df_filteredD3[D])
meanD3 = np.mean(df_sortedD3)
sdD3 = np.std(df_sortedD3)
modeD3 = df_filteredD3[D].mode
print(modeD3)

df_sortedD4 = np.sort(df_filteredD4[D])
meanD4 = np.mean(df_sortedD4)
sdD4 = np.std(df_sortedD4)
modeD4 = df_filteredD4[D].mode
print(modeD4)

df_sortedL1 = np.sort(df_filteredL1[L])
meanL1 = np.mean(df_sortedL1)
sdL1 = np.std(df_sortedL1)
modeL1 = df_filteredL1[L].mode
print(modeL1)

df_sortedL2 = np.sort(df_filteredL2[L])
meanL2 = np.mean(df_sortedL2)
sdL2 = np.std(df_sortedL2)
modeL2 = df_filteredL2[L].mode
print(modeL2)

df_sortedL3 = np.sort(df_filteredL3[L])
meanL3 = np.mean(df_sortedL3)
sdL3 = np.std(df_sortedL3)
modeL3 = df_filteredL3[L].mode
print(modeL3)

df_sortedP = np.sort(df_filteredP[P])
meanP = np.mean(df_sortedP)
sdP = np.std(df_sortedP)
modeP = df_filteredP[P].mode
print( modeP)
''' 
plt.plot(norm.pdf(df_sortedD, meanD, sdD))
plt.plot(norm.pdf(df_sortedL1, meanL1, sdL1))
plt.plot(norm.pdf(df_sortedL2, meanL2, sdL2))
plt.plot(norm.pdf(df_sortedL3, meanL3, sdL3))
plt.plot(norm.pdf(df_sortedP, meanP, sdP))
'''
'''
plt.boxplot(df_sortedD, vert=False)
plt.boxplot(df_sortedL1, vert=False)
plt.boxplot(df_sortedL2, vert=False)
plt.boxplot(df_sortedL3, vert=False)
plt.boxplot(df_sortedP, vert=False)
'''
opt_binND1 = math.ceil(math.sqrt(len(df_sortedD1))+1)
opt_binND2 = math.ceil(math.sqrt(len(df_sortedD2))+1)
opt_binND3 = math.ceil(math.sqrt(len(df_sortedD3))+1)
opt_binND4 = math.ceil(math.sqrt(len(df_sortedD4))+1)
opt_binNL1 = math.ceil(math.sqrt(len(df_sortedL1))+1)
opt_binNL2 = math.ceil(math.sqrt(len(df_sortedL2))+1)
opt_binNL3 = math.ceil(math.sqrt(len(df_sortedL3))+1)
opt_binNP = math.ceil(math.sqrt(len(df_sortedP))+1)

plt.hist(df_sortedD1, bins=opt_binND1, color = "red")
plt.hist(df_sortedD2, bins=opt_binND2, color = "red")
plt.hist(df_sortedD3, bins=opt_binND3, color = "red")
plt.hist(df_sortedD4, bins=opt_binND4, color = "red")
plt.hist(df_sortedL1, bins=opt_binNL1, color ='blue')
plt.hist(df_sortedL2, bins=opt_binNL2, color='orange')
plt.hist(df_sortedL3, bins=opt_binNL3, color = 'green')
plt.hist(df_sortedP, bins=opt_binNP, color = 'darkblue')

plt.xlabel('Length Measurements (mm)')
plt.ylabel('Frequency')
plt.title('All datasets')
plt.xticks(np.arange(0, 250, 10))
plt.yticks(np.arange(0, 50, 10))
red_patch = mpatches.Patch(color='red', label='Diameter')
green_patch = mpatches.Patch(color='green', label='3rd Length')
orange_patch = mpatches.Patch(color='orange', label='2nd Length')
blue_patch = mpatches.Patch(color='blue', label='1st Length')
Dblue_patch = mpatches.Patch(color='darkblue', label='Pitch')
plt.legend(handles=[red_patch, green_patch, blue_patch, Dblue_patch, orange_patch])
plt.grid()
plt.show()

#df.reset_index().plot.scatter(x = 'index', y = D, c=df[B].map(colors))


