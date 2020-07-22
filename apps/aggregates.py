import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from apps.data import df
from app import app


aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)


data = [dict(
  type = 'bar',
  x = df['Date'].to_list(),
  y = df['Total Respirators'].to_list(),
  color=df["Hospital Name"].unique(),
    barmode="group",
#   mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = df['Date'].to_list(),
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True)
    ]
  )]
)]

layout_dict = dict(
  title = '<b>Respirators Stats</b>',
  color=df["Hospital Name"].unique(),
    barmode="group",
  xaxis = dict(title = 'Date'),
  yaxis = dict(title = 'Total Respirators', range = [0,2500]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)


fig_dict = dict(data=data, layout=layout_dict)


layout = html.Div([
                html.Div(className='page-header-container',children=[
                    html.H1('Aggregates', className='page-header',),
                ]),
                html.Div(className='large-graph-container',children=[
                    html.H2('Aggregates based on time and respirator amount', className='graph-header',),
                      dcc.Graph(id = 'plot', figure = fig_dict)
                ]),
                ])

