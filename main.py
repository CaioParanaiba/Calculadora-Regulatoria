from flask import Flask, render_template
from configure import configure_all


# inicializar o flask
app = Flask(__name__)

configure_all(app)


@app.route('/sobre')
def pagina_sobre():
    return render_template('sobre.html')

# Execução
app.run(debug=True) # modo desenvolvedor
