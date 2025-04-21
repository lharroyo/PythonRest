import dash
from dash import dcc, html, dash_table
import pandas as pd
import requests

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Función para obtener datos de la API
def fetch_data():
    response = requests.get("http://127.0.0.1:5000/hiredemployees/byquarter")  # Cambia la URL según sea necesario
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error fetching data", "results": []}  # Retornar un mensaje de error si hay un problema

# Obtener los datos
data = fetch_data()
results = data.get("results", [])

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(results)

# Crear el layout de la aplicación
app.layout = html.Div([
    html.H1(data.get("message", "Hires Data")),
    dash_table.DataTable(
        id='table',
        columns=[
            {"name": "Department", "id": "department"},
            {"name": "Job", "id": "job"},
            {"name": "Quarter", "id": "quarter"},
            {"name": "Hires", "id": "hires"}
        ],
        data=df.to_dict('records'),
        page_size=10,  # Número de filas por página
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)