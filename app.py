import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
# <--<h1 id="iris-header">IRIS Systems</h1> -->

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>IRIS Systems</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <header>
            <img id="header-img" src="/assets/iris-image.png" alt="iris image"/>
            <nav id="nav-link-container">
                <a href="/">Overview </a>
                <a href="/aggregates">Aggregates </a>
                <a href="/predictions">Predictions</a>
            </nav> 
        </header>
        
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>IRIS Systems 2020</div>
    </body>
</html>
'''

# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)