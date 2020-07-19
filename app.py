import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px


df = pd.DataFrame({
    "Hospital Name": ["Hospital 1", "Hospital 1", "Hospital 2", "Hospital 2", "Hospital 3", "Hospital 3"],
    "City": ["SF", "SF", "NYC", "NYC", "ATL", "ATL"],
    "State": ["CA", "CA", "NY", "NY", "GA", "GA"],
    "Zipcode": [94117, 94001, 10001, 10021, 30336, 30301],
    "Total Gowns": [500, 700, 2000, 1500, 700, 1000],
    "Total Masks": [4000, 3500, 10000, 8460, 5000, 7000],
    "Total Gloves": [1000, 900, 2000, 1700, 1200, 1400],
    "Total Respirators": [500, 300, 1000, 700, 650, 1400],
    "Date":  ["06/01/2020", "06/02/2020", "06/01/2020", "06/02/2020", "06/01/2020", "06/02/2020"]
})

# Convert the datetime
df['Date'] = pd.to_datetime(df['Date'])


app = dash.Dash()

# ------ Respirators -------- #

# Bargraph 
overview_bar_respirators = px.bar(df, x="Date", y="Total Respirators", color="Hospital Name", barmode="group")
overview_bar_respirators.update_xaxes(rangeslider_visible=True)

# Line graph
overview_line_respirators = px.line(df, x="Date", y="Total Respirators", color="Hospital Name")
overview_line_respirators.update_xaxes(rangeslider_visible=True)

# scatter plots

overview_scatter_respirators = px.scatter(df, x="Date", y="Total Respirators", color="Hospital Name")
overview_scatter_respirators.update_xaxes(rangeslider_visible=True)



# Step 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'bar', figure = overview_bar_respirators),
                dcc.Graph(id='line', figure = overview_line_respirators),
                dcc.Graph(id='scatter', figure = overview_scatter_respirators)
                      ])

# Step 5. Add callback functions


# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)