import csv
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px
df = pd.read_csv('data.csv')

df2=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
fig=px.scatter(df2,x='student_id',y='level',color='attempt')

fig.show()