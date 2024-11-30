from flask import Flask, render_template
from configure import configure_all

# inicializar o flask
app = Flask(__name__)

configure_all(app)


@app.route('/sobre')
def pagina_sobre():
    return render_template('sobre.html')

@app.route('/equipe')
def pagina_membros():
    return render_template('equipe.html')

@app.route('/manual')
def pagina_manual():
    return render_template('manual.html')

@app.route('/termos')
def termos_e_condicoes():
    return render_template('termos_e_condicoes.html')

# Execução
app.run(debug=True) # modo desenvolvedor
