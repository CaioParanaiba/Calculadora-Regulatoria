from database import db

class Subcategoria(db.Model):
    __tablename__ = 'subcategorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    definicao = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    tipo_preco = db.Column(db.String(100))
    formula_quantidade = db.Column(db.String(200))
    preco_variavel = db.Column(db.String(50))

    variaveis = db.relationship('Variavel', backref='subcategoria', lazy=True)
    subcategorias_personalizadas = db.relationship('SubcategoriaPersonalizada', backref='subcategoria', lazy=True)

    def __repr__(self):
        return f'<Subcategoria {self.nome}>'
