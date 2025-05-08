from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# --- Ejercicio 1 con PRG  ---
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Procesa los datos del formulario
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        asist = float(request.form['asist'])

        promedio = round((n1 + n2 + n3) / 3, 1)
        estado   = 'APROBADO' if (promedio >= 40 and asist >= 75) else 'REPROBADO'

        # Redirigimos a la misma ruta pero pasando los resultados por query string
        return redirect(url_for('ejercicio1',
                                promedio=promedio,
                                estado=estado))

    # Si es GET, lee los parámetros
    promedio = request.args.get('promedio')
    estado   = request.args.get('estado')
    # Lo pasa al template; si no están definidos, el template los ignora
    return render_template('ejercicio1.html',
                           promedio=promedio,
                           estado=estado)


# --- Ejercicio 2 con PRG  ---
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Lee los tres nombres
        nombres = [
            request.form['n1'].strip(),
            request.form['n2'].strip(),
            request.form['n3'].strip()
        ]
        nombre_largo = max(nombres, key=len)
        longitud     = len(nombre_largo)

        # Redirigimos a la misma ruta con resultados en query string
        return redirect(url_for('ejercicio2',
                                nombre_largo=nombre_largo,
                                longitud=longitud))

    # En GET, lee los parámetros si existen
    nombre_largo = request.args.get('nombre_largo')
    longitud     = request.args.get('longitud')
    return render_template('ejercicio2.html',
                           nombre_largo=nombre_largo,
                           longitud=longitud)


if __name__ == '__main__':
    app.run(debug=True)

