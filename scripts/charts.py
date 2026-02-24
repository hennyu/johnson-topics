#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly.graph_objects as go
import pandas as pd
from os.path import join


# read metadata
wdir = "/home/ulrike/Git/johnson-topics"
md_filepath = "data/letters-leipzig-metadata.csv"
md = pd.read_csv(join(wdir, md_filepath), sep=",", index_col=0, header=0)

# plot letters by year
start_year = min(md.year[md.year != 0])
end_year = max(md.year)

x_labels = [0] + list(range(start_year,end_year+1,1))
y_values = []

for year in x_labels:
	val = len(md[md.year == year])
	y_values.append(val)
	
x_labels = ["unknown" if i==0 else str(i) for i in x_labels]

fig = go.Figure([go.Bar(x=x_labels, y=y_values)])
fig.update_layout(width=600,height=400)
fig.update_xaxes(tickangle=270, title="year")
fig.update_yaxes(title="number of letters")
fig.show()

print("done")
