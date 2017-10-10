import plotly.plotly as py
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='yangbo', api_key='Kon3H9RnCvNDS3lDPIXi')

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis data'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[4, 5, 6],
    name='yaxis2 data',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='yaxis title'
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multiple-axes-double')
