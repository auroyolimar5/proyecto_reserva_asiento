from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario para almacenar las reservas
reservas = {
    'Lunes': {},
    'Martes': {},
    'Miércoles': {},
    'Jueves': {},
    'Viernes': {}
}

puestos = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5']


@app.route('/')
def index():
    return render_template('index.html', reservas=reservas, puestos=puestos)


@app.route('/reservar', methods=['POST'])
def reservar():
    dia = request.form['dia']
    puesto = request.form['puesto']
    nombre = request.form['nombre']
    if puesto in reservas[dia]:
        return "El puesto ya está reservado", 400
    reservas[dia][puesto] = nombre
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
