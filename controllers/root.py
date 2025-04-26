from flask import Blueprint, render_template_string

rootpath = Blueprint('root', __name__)

@rootpath.route('/')
def index():
    routes = [
        {'name': 'Departamentos', 'url': '/departments'},
        {'name': 'Empleos', 'url': '/jobs'},
        {'name': 'Empleados Contratados', 'url': '/hiredemployees'}
    ]
    html = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Menú de API</title>
    </head>
    <body>
        <h1>Menú de API</h1>
        <ul>
        {% for route in routes %}
            <li><a href="{{ route.url }}">{{ route.name }}</a></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, routes=routes)
