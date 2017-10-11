import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=[1, 2, 3, 5.5, 10],
    y=[10, 8, 6, 4, 2],
    width = [0.8, 0.8, 0.8, 3.5, 4]
)

data = [trace0]

fig = go.Figure(data=data)
py.iplot(fig, filename='width-bar')
