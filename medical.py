import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
df = pd.read_csv('medical_examination.csv',index_col='id')
df['overweight'] = (df['weight']/(df['height']/100)**2).apply(lambda x:1 if x>=25 else 0)
df['gluc']=df['gluc'].apply(lambda x:0 if x==1 else 1)
df['cholesterol']=df['cholesterol'].apply(lambda x:0 if x==1 else 1)
selected_cols = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
df_cat = pd.melt(df,id_vars = ['cardio'], value_vars = selected_cols)
df_cat['total']=1
df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value'].count())
df_cat=df_cat.rename(columns={'value': 'total'}).reset_index()
sns.set_theme(style='dark')
fig = sns.catplot(x = "variable", y = "total", data = df_cat, hue ="value", kind = "bar", col = "cardio").fig 
fig.savefig('catplot.png')
df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
             (df['height'] >= df['height'].quantile(0.025)) &
             (df['height'] <= df['height'].quantile (0.975)) &
             (df ['weight'] >= df ['weight'].quantile(0.025)) &
             (df ['weight'] <= df ['weight'].quantile(0.975))]
corr=df_heat.corr()
mask = np.triu(corr)
fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(corr, linewidths=1, annot = True, square= True, mask = mask, fmt=".1f", center =0.08, cbar_kws = {"shrink":0.5})
fig.savefig('heatmap.png')