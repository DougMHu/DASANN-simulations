#------------------------------------------------------------
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

x = ['A', 'B', 'C', 'D', 'E']
y = ['W', 'X', 'Y', 'Z']

#       x0    x1    x2    x3    x4
z = [[0.00, 0.00, -0.75, 0.75, 0.00],  # y0
     [0.00, 0.00, 0.75, 0.75, 0.00],  # y1
     [0.75, 0.75, 0.75, 0.75, 0.75],  # y2
     [0.00, 0.00, 0.00, 0.75, 0.00]]  # y3

annotations = []
for n, row in enumerate(z):
    for m, val in enumerate(row):
        var = z[n][m]
        if (var != 0):
            annotations.append(
                dict(
                    text=str(val),
                    x=x[m], y=y[n],
                    xref='x1', yref='y1',
                    font=dict(color='white' if val > 0.5 else 'black'),
                    showarrow=False)
                )

colorscale = [[0, '#FFFFFF'], [1, '#000000']]  # custom colorscale
trace = go.Heatmap(x=x, y=y, z=z, colorscale=colorscale, showscale=False)

fig = go.Figure(data=[trace])
fig['layout'].update(
    title="Annotated Heatmap",
    annotations=annotations,
    xaxis=dict(ticks='', side='top'),
    # ticksuffix is a workaround to add a bit of padding
    yaxis=dict(ticks='', ticksuffix='  '),
    width=700,
    height=700,
    autosize=False)

fileName = plot(fig, filename='Annotated Heatmap.html')