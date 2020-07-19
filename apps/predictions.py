import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from apps.data import df
from app import app



# Line graph
prediction_line_respirators = px.line(df, x="Date", y="Total Respirators", color="Hospital Name")
prediction_line_respirators.update_xaxes(rangeslider_visible=True)


layout = html.Div([
                dcc.Graph(id='line', figure = prediction_line_respirators),
                
                      ])