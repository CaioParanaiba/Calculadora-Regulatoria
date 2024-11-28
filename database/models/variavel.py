from database import db

class Variavel(db.Model):
    __tablename__ = 'variaveis'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # 'float' ou 'int'
    descricao = db.Column(db.Text)
    subcategoria_id = db.Column(db.Integer, db.ForeignKey('subcategorias.id'), nullable=False)

    valor_variaveis = db.relationship('ValorVariavel', backref='variavel', lazy=True)

    def __repr__(self):
        return f'<Variavel {self.nome}>'
