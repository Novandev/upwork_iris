
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from components import Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd


#data 


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


