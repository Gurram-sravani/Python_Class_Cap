import pandas as pd
import numpy as np
d1=pd.read_csv(r'C:\Users\srgurram\Downloads\d2.csv')
model = pd.read_csv(r'C:\Users\srgurram\Downloads\d2.csv')
model = model.drop(columns=model.columns[0])
model1 = model.copy()
for i in model1.columns:
    if model1[i].dtypes == 'object':
        model1[i].fillna('NA', inplace=True)
    else:
        model1[i].fillna(0, inplace=True)

def fun():
    return model1
