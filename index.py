import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home,aggregates,predictions


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    # elif pathname == '/aggregates':
    #     return aggregates.layout
    # elif pathname == '/predictions':
    #     return predictions.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)