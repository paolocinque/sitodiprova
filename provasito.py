from flask import Flask, render_template, request
    
app = Flask(__name__)

@app.route('/')
def menuatendina():
    return render_template('menuatendina.html')
    
    
@app.route('/calcola', methods=['POST'])

def calcola_risultato(prezzo):
    periodo = int(request.form['Periodo di Copertura']) 
    tipologia = int(request.form['Tipologia Miele'])      
    zona_geografica = int(request.form['Area Geografica'])

    prezzo == periodo + tipologia + zona_geografica

    return render_template ('calcola.html')
   