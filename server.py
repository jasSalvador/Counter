from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'count' in session: #preguntamos si existe count en session
        session['count'] += 1 #si existe, sumamos 1 a lo q antes teniamos
        #print('la llave existe!')
    else:
        session['count'] = 0 #si no existe, entonces inicialzamos el count en 1
    #print("la llave 'key_name' NO existe")
    return render_template('index.html', count= session['count'])


#para q sume 2
@app.route('/2')
def index2():
    session['count'] += 1
    return redirect('/')


#borrar sesion
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


#para que sume el numero q se ingresa
@app.route("/add/number", methods=['POST'])
def count_numb():
    number = int(request.form['cantidad'])
    session["count"] += (number-1) #Aquí hacemos numero - 1 porque al momento de hacer el redirect se suma uno de todas formas
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)