import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

app = dash.Dash()



# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)