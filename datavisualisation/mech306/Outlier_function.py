import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def detect_outliers(data):
    outliers=[]
    #Using Z-score, the outliers are most likely found at a score above or below 3, which generally corresponds to 99% confidence interval

    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z = (i-mean)/std
        if np.abs(z) > threshold:
            outliers.append(i)

    return outliers

def remove_outlier(data):
    index = 0
    y = detect_outliers(data)

    pos = len(y) - 1

    while pos < len(y):
        for i in data:
            if i == y[pos]:
                np.delete(data, index, 0)
            index = index + 1
        pos = pos + 1
    return data

#filtering outliers using Percentiles
qlow_L= df[L].quantile(0.01)
qhi_L= df[L].quantile(0.99)

df_filtered = df[(df[L] < qhi_L) & (df[L] > qlow_L)]

#Renaming headers - cannot work with version it is only a temporary copy
correct_df = df_filtered.copy()
correct_df.rename(columns={B: 'Blocks', L:'Length (mm)', D:'Diameter (mm)', P:'Pitch (mm)'}, inplace = True)
print(correct_df)