import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from apps.data import df
from app import app



config = {
   
    'displaylogo': False
}

# ------ Respirators -------- #

# Bargraph 
overview_bar_respirators = px.bar(df, x="Date", y="Total Respirators", color="Hospital Name", barmode="group")
overview_bar_respirators.update_xaxes(rangeslider_visible=True)

# Line graph
overview_line_respirators = px.line(df, x="Date", y="Total Respirators", color="Hospital Name")
overview_line_respirators.update_xaxes(rangeslider_visible=True)

# Scatter plots

overview_scatter_respirators = px.scatter(df, x="Date", y="Total Respirators", color="Hospital Name")
overview_scatter_respirators.update_xaxes(rangeslider_visible=True)

# Pie charts

overview_pie_respirators = px.pie(df, values="Total Respirators", names="State")


# Step 4. Create a Dash layout
layout = html.Div([
      html.Div(className='page-header-container',children=[
            html.H1('Overview', className='page-header',),
      ]),
      html.Div(className='total-box-container',children=[
            html.Div(className='total-container',children=[
            html.H2('Daily Totals', className='totals-header',),
            html.Div(id='total-numbers-container',children=[
                  html.Div(className='total-numbers',children=[
                        html.H3('Total Masks', className='totals-header',),
                        html.H4('3000', className='totals-total',),   
                  ]),
                  html.Div(className='total-numbers',children=[
                        html.H3('Total Respirators', className='totals-header',),
                        html.H4('1500', className='totals-total',),   
                  ]),
                  html.Div(className='total-numbers',children=[
                        html.H3('Total Ventilators', className='totals-header',),
                        html.H4('2200', className='totals-total',),   
                  ]),
                  html.Div(className='total-numbers',children=[
                     html.H3('Total Gloves', className='totals-header',),
                     html.H4('2500', className='totals-total',),    
                  ]),

            ])

      ]),
      ]),
      
      html.Div(className='plot-container',children=[
            html.Div(className='feature-container',children=[
                  html.H2('Bar Graph', className='graph-header',),
                  dcc.Graph(id = 'bar',className='figure', figure = overview_bar_respirators)
            ]),
            html.Div(className='feature-container',children=[
                  html.H2('Line Graph', className='graph-header',),
                  dcc.Graph(id='line',className='figure', figure = overview_line_respirators),
            ]),
            
      ]),
      
      html.Div(className='plot-container',children=[
            html.Div(className='feature-container',children=[
                  html.H2('Scatter Plot', className='graph-header',),
            dcc.Graph(id='scatter',className='figure', figure = overview_scatter_respirators),
            ]),
            html.Div(className='feature-container',children=[
                  html.H2('Pie Graph', className='graph-header',),
            dcc.Graph(id='pie',className='figure', figure = overview_pie_respirators)
            ])
            
      ]),
      
                      ])