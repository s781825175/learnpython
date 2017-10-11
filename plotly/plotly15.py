import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4]

trace1 = {
  'x': x,
  'y': [1, 4, 9, 16],
  'name': 'Trace1',
  'type': 'bar'
};
trace2 = {
  'x': x,
  'y': [6, -8, -4.5, 8],
  'name': 'Trace2',
  'type': 'bar'
};
trace3 = {
  'x': x,
  'y': [-15, -3, 4.5, -8],
  'name': 'Trace3',
  'type': 'bar'
 }
 
trace4 = {
  'x': x,
  'y': [-1, 3, -3, -4],
  'name': 'Trace4',
  'type': 'bar'
 }
 
data = [trace1, trace2, trace3, trace4];
layout = {
  'xaxis': {'title': 'X axis'},
  'yaxis': {'title': 'Y axis'},
  'barmode': 'relative',
  'title': 'Relative Barmode'
};
py.iplot({'data': data, 'layout': layout}, filename='barmode-relative')
