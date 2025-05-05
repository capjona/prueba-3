from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# --- Ejercicio 1 con PRG ---
@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        asist = float(request.form['asist'])

        promedio = round((n1 + n2 + n3) / 3, 1)
        estado   = 'APROBADO' if (promedio >= 40 and asist >= 75) else 'REPROBADO'

        # Redirige con los valores en la URL
        return redirect(url_for('resultado1',
                                promedio=promedio,
                                estado=estado))
    return render_template('ejercicio1.html')

@app.route('/resultado1')
def resultado1():
    promedio = request.args.get('promedio')
    estado   = request.args.get('estado')
    if not promedio or not estado:
        # Si faltan parámetros, volvemos al formulario
        return redirect(url_for('ejercicio1'))
    # Renderiza la misma plantilla pero ya con datos
    return render_template('ejercicio1.html',
                           promedio=promedio,
                           estado=estado)


# --- Ejercicio 2 con PRG ---
@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        nombres = [
            request.form['n1'].strip(),
            request.form['n2'].strip(),
            request.form['n3'].strip(),
        ]
        nombre_largo = max(nombres, key=len)
        longitud     = len(nombre_largo)

        return redirect(url_for('resultado2',
                                nombre_largo=nombre_largo,
                                longitud=longitud))
    return render_template('ejercicio2.html')

@app.route('/resultado2')
def resultado2():
    nl  = request.args.get('nombre_largo')
    lon = request.args.get('longitud')
    if not nl or not lon:
        return redirect(url_for('ejercicio2'))
    return render_template('ejercicio2.html',
                           nombre_largo=nl,
                           longitud=lon)


if __name__ == '__main__':
    app.run(debug=True)

