import dash
from dash import dcc, html, dash_table
import pandas as pd
import requests

app = dash.Dash(__name__)

def fetch_hires_data():
    response = requests.get("https://pythonemployees.azurewebsites.net/hiredemployees/byquarter")
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error fetching data", "results": []}

def fetch_average_hires_data():
    response = requests.get("https://pythonemployees.azurewebsites.net/hiredemployees/byaveragehires")
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error fetching data", "results": []}

hires_data = fetch_hires_data()
hires_results = hires_data.get("results", [])

df_hires = pd.DataFrame(hires_results)

df_hires_pivot = df_hires.pivot_table(
    index=['department', 'job'],
    columns='quarter',
    values='hires',
    aggfunc='sum',
    fill_value=0
).reset_index()

df_hires_pivot.columns.name = None
df_hires_pivot = df_hires_pivot.rename(columns={1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})

average_hires_data = fetch_average_hires_data()
average_hires_results = average_hires_data.get("results", [])

df_average_hires = pd.DataFrame(average_hires_results)

app.layout = html.Div([
    html.H1("Hires Data"),
    dcc.Tabs([
        dcc.Tab(label='Hires by Job and Department', children=[
            dash_table.DataTable(
                id='hires_table',
                columns=[
                    {"name": "Department", "id": "department"},
                    {"name": "Job", "id": "job"},
                    {"name": "Q1", "id": "Q1"},
                    {"name": "Q2", "id": "Q2"},
                    {"name": "Q3", "id": "Q3"},
                    {"name": "Q4", "id": "Q4"}
                ],
                data=df_hires_pivot.to_dict('records'),
                page_size=20,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},
            )
        ]),
        dcc.Tab(label='Departments Above Average Hires', children=[
            dash_table.DataTable(
                id='average_hires_table',
                columns=[
                    {"name": "Department ID", "id": "department_id"},
                    {"name": "Department Name", "id": "department_name"},
                    {"name": "Hires", "id": "hires"}
                ],
                data=df_average_hires.to_dict('records'),
                page_size=20,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run(debug=True)