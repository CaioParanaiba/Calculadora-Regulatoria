from database import db

class Custo(db.Model):
    __tablename__ = 'custos'

    id = db.Column(db.Integer, primary_key=True)
    valor_custo = db.Column(db.Float, nullable=False)
    subcategoria_personalizada_id = db.Column(db.Integer, db.ForeignKey('subcategorias_personalizadas.id'), nullable=False)

    def __repr__(self):
        return f'<Custo {self.subcategoria_personalizada.nome_personalizado}: {self.valor_custo}>'
