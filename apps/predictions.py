import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from apps.clustering import df_clusters
from apps.data import df
from apps.VARMA import hospital_1_yhat,hospital_2_yhat,hospital_3_yhat
from app import app



# Line graph LSTM/ ARIMA  models
prediction_line_respirators = px.line(df, x="Date", y="Total Respirators", color="Hospital Name")
prediction_line_respirators.add_scatter(x=df['Date'], y=hospital_1_yhat[0], mode='lines',name="Hospital 1 Forecast")
prediction_line_respirators.add_scatter(x=df['Date'], y=hospital_2_yhat[0], mode='lines',name="Hospital 2 Forecast")
prediction_line_respirators.add_scatter(x=df['Date'], y=hospital_3_yhat[0], mode='lines',name="Hospital 3 Forecast")
prediction_line_respirators.update_xaxes(rangeslider_visible=True)


layout = html.Div([
      html.Div(className='page-header-container',children=[
            html.H1('Predictions', className='page-header',),
      ]),
      html.Div(className='large-graph-container',children=[
            html.H2('Forecast', className='graph-header',),
            dcc.Graph(id='line', figure = prediction_line_respirators),
      ]),
      html.Div(className='page-header-container-cluster',children=[
            html.H1('Clusters', className='page-header',),
      ]),
      html.Div(className='large-graph-container',children=[
            
      ]),
      html.Div(className='total-box-container',children=[
            html.Div(className='total-container',children=[
            html.H2('Hospital Clusters', className='totals-header',),
            html.Div(id='total-numbers-container',children=[
                  html.Div(className='total-numbers',children=[
                        html.H3('Cluster 1', className='totals-header',),
                        html.H4('Hospital 1', className='totals-total',),   
                  ]),
                  html.Div(className='total-numbers',children=[
                        html.H3('Cluster 2', className='totals-header',),
                        html.H4('Hospital 2', className='totals-total',),
                        html.H4('Hospital 3', className='totals-total',),      
                  ]),

            ])

      ]),
      ]),
      
                
                      ])