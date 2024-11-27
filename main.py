from flask import Flask

# importa os conjuntos de rotas
from routes.home import home_route
from routes.empresa import empresa_route

# inicializar o flask
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(empresa_route, url_prefix='/empresa')

@app.route('/sobre')
def pagina_sobre():
    return """
    <h1>Sobre a Calculadora de Impacto Regulatório</h1>
    <p>
    A <strong>Calculadora de Impacto Regulatório</strong> é uma aplicação web 
    desenvolvida em Python utilizando o framework Flask. Seu objetivo é 
    auxiliar empresas na análise e compreensão dos custos associados a 
    regulamentações específicas que impactam suas operações.
    </p>
    <p>
    Com esta ferramenta, os usuários podem calcular e visualizar os custos de 
    conformidade e os custos financeiros diretos decorrentes de leis e 
    regulamentações, oferecendo uma análise detalhada para tomada de decisão 
    estratégica. 
    </p>
    <p>
    A Calculadora foi projetada para ser intuitiva e eficiente, permitindo às 
    empresas entenderem melhor os impactos financeiros de suas obrigações 
    regulatórias e planejarem suas operações de maneira mais informada.
    </p>
    """

# Execução
app.run(debug=True) # modo desenvolvedor
