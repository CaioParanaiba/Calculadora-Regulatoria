from flask import Flask, render_template
from configure import configure_all
import logging

logging.basicConfig(
    filename='app.log',  # Nome do arquivo de log
    level=logging.INFO,  # Nível do log
    format='%(asctime)s %(levelname)s %(message)s'
)

# inicializar o flask
app = Flask(__name__)

configure_all(app)


@app.route('/sobre')
def pagina_sobre():
    return render_template('sobre.html')

# Execução
app.run(debug=True) # modo desenvolvedor
