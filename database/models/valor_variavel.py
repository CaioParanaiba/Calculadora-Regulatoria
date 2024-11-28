from database import db

class ValorVariavel(db.Model):
    __tablename__ = 'valor_variaveis'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    subcategoria_personalizada_id = db.Column(db.Integer, db.ForeignKey('subcategorias_personalizadas.id'), nullable=False)
    variavel_id = db.Column(db.Integer, db.ForeignKey('variaveis.id'), nullable=False)

    def __repr__(self):
        return f'<ValorVariavel {self.variavel.nome}: {self.valor}>'
