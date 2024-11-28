from database import db

class SubcategoriaPersonalizada(db.Model):
    __tablename__ = 'subcategorias_personalizadas'

    id = db.Column(db.Integer, primary_key=True)
    nome_personalizado = db.Column(db.String(150))
    definicao_personalizada = db.Column(db.Text)
    subcategoria_id = db.Column(db.Integer, db.ForeignKey('subcategorias.id'), nullable=False)

    valor_variaveis = db.relationship('ValorVariavel', backref='subcategoria_personalizada', lazy=True)
    custos = db.relationship('Custo', backref='subcategoria_personalizada', lazy=True)

    def __repr__(self):
        return f'<SubcategoriaPersonalizada {self.nome_personalizado or self.subcategoria.nome}>'
