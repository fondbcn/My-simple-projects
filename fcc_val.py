import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])
df = df[(df['value']<df['value'].quantile(0.975))&(df['value']>df['value'].quantile(0.025))]
df_bar = df.copy()
ln_plt = df.plot.line()
fig =ln_plt.get_figure()
# fig.savefig('out1.png')
df_bar = df.copy()
df ["month"]= df.index.month
df ["year"]=df.index.year
df_bar = df.groupby ( ["year", "month"]) ["value"].mean().unstack()
br_plt = df_bar.plot.bar()
fig =br_plt.get_figure()
# fig.savefig('out2.png')
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
df_box ["month_num"] = df_box["date"].dt.month
df_box= df_box.sort_values ("month_num")
fig, axes= plt.subplots (nrows=1, ncols=2, figsize=(10,5))
axes [0]=sns.boxplot (x=df_box ["year"], y=df_box["value"], ax = axes[0])
axes [1] = sns.boxplot (x=df_box ["month"], y=df_box["value"], ax = axes [1])
# fig.savefig('out3.png')