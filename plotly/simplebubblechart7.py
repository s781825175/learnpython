import plotly.plotly as py
import plotly.graph_objs as go

data = [
    {
        'x': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'y': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'mode': 'markers',
        'marker': {
            'color': [120, 125, 130, 135, 140, 145],
            'size': [15, 30, 55, 70, 90, 110],
            'showscale': True
        }
    }
]

py.iplot(data, filename='scatter-colorscale')
