import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from apps.data import df
from app import app



# Line graph LSTM/ ARIMA  models
prediction_line_respirators = px.line(df, x="Date", y="Total Respirators", color="Hospital Name")
prediction_line_respirators.add_scatter(x=df['Date'], y=df['Total Respirators'] -100, mode='lines',name="Predictions")
prediction_line_respirators.update_xaxes(rangeslider_visible=True)


layout = html.Div([
      html.Div(className='page-header-container',children=[
            html.H1('Predictions', className='page-header',),
      ]),
      html.Div(className='large-graph-container',children=[
            html.H2('LSTM Based Predictions', className='graph-header',),
            dcc.Graph(id='line', figure = prediction_line_respirators),
      ]),
      
                
                      ])