import plotly.plotly as py
import plotly.graph_objs as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

data = [go.Bar(
            x=x,
            y=y,
            text=['27% market share', '24% market share', '19% market share'],
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

py.iplot(data, filename='bar-direct-labels')
