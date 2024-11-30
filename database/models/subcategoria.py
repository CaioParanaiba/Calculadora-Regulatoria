from database.database import db
from database.models.empresa import Empresa
from peewee import Model, CharField, TextField, FloatField, AutoField, ForeignKeyField

class BaseModel(Model):
    class Meta:
        database = db

class SubCategoria(BaseModel):
    id = AutoField()  # Chave primária
    categoria = CharField(max_length=100)  # varchar(100)
    name = CharField(max_length=100)  # varchar(100)
    definicao = TextField()  # text
    tipo_preco = CharField(max_length=150, null=True)  # Permite nulo
    formula = TextField()  # text
    preco_variavel = TextField()  # float
    quantidades_json = TextField()  # text (para armazenar JSON como string)
    
class SubCategoriaPer(BaseModel):
    id = AutoField()  # Chave primária
    name = CharField(max_length=100)
    categoria = CharField(max_length=100)
    definicao = TextField()
    formula = TextField()
    preco_variavel = TextField()
    quantidades_json = TextField()
    empresa = ForeignKeyField(Empresa, backref="subcategorias_per")

valores_iniciais = [
    {
        "categoria": "Custos de Conformidade",
        "name": "Atrasos (Custos trabalhistas)",
        "definicao": "Custos incorridos em função de atrasos administrativos que resultem em despesas trabalhistas.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Atrasos (Custo do investimento)",
        "definicao": "Custos de oportunidade em função do investimento realizado para iniciar uma operação.",
        "formula": "tempo",
        "preco_variavel": '{"investimento": 0}',
        "quantidades_json": '{"tempo": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Atrasos (Perda de receita)",
        "definicao": "Custos incorridos em função de atrasos administrativos que resultem em perda de receita.",
        "formula": "tempo",
        "preco_variavel": '{"custo_de_perda_receita": 0}',
        "quantidades_json": '{"tempo": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Permissão",
        "definicao": "Custos incorridos para solicitar e manter a permissão para realizar uma atividade.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Taxas",
        "definicao": "Qualquer taxa diretamente relacionada com a regulamentação aplicada, ou alterações no valor das taxas após a regulamentação.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_da_taxa": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Outros (Conformidade)",
        "definicao": "Qualquer outro custo de conformidade/compliance enfrentado pelas empresas que não se enquadre em uma das categorias acima.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Outros (Financeiro)",
        "definicao": "Qualquer outro custo financeiro direto enfrentado pelas empresas que não se enquadre em uma das categorias acima.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_nominal": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Notificação",
        "definicao": "Custos incorridos quando empresas precisam relatar determinados eventos a uma autoridade reguladora.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Registros",
        "definicao": "Custos incorridos para manter atualizados os documentos e/ou registros.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Publicação e Documentação",
        "definicao": "Custos incorridos para a produção de documentos para terceiros.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Despesas de capital decorrentes da norma",
        "definicao": "Custos de capital relacionados com mudanças estruturais, inclusive intervenções de infraestrutura.",
        "formula": "unitaria",
        "preco_variavel": '{"custo_de_capital_anual": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Compras",
        "definicao": "Custos ao adquirir um serviço (ex: consultoria) ou um produto para cumprir uma regulamentação.",
        "formula": "n_compras",
        "preco_variavel": '{"custo_de_compra": 0}',
        "quantidades_json": '{"n_compras": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Cumprimento Legal",
        "definicao": "Custos incorridos para cooperar com auditorias, inspeções e atividades regulatórias.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Treinamento/Capacitação",
        "definicao": "Custos incorridos para manter-se atualizado com os requisitos regulatórios.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos de Conformidade",
        "name": "Processual",
        "definicao": "Custos não administrativos impostos por alguma regulamentação.",
        "formula": "n_funcionarios * horas_dedicas * n_interacoes",
        "preco_variavel": '{"custo_de_mao_de_obra": 0}',
        "quantidades_json": '{"n_funcionarios": 0, "horas_dedicas": 0, "n_interacoes": 0}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Impostos",
        "definicao": "Qualquer imposto diretamente relacionado com a regulamentação aplicada, ou qualquer alteração no valor dos impostos após alteração/implementação da regulamentação.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_do_imposto": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Tarifas",
        "definicao": "Qualquer tarifa diretamente relacionada com a regulamentação aplicada, ou qualquer alteração no valor de tarifas após alteração/implementação da regulamentação.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_da_tarifa": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Emolumentos",
        "definicao": "Qualquer emolumento diretamente relacionado com a regulamentação aplicada, ou qualquer alteração no valor dos emolumentos após alteração/implementação da regulamentação.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_dos_emolumentos": 0}',
        "quantidades_json": '{"unitaria": 1}'
    },
    {
        "categoria": "Custos Financeiros Diretos",
        "name": "Outorgas",
        "definicao": "Qualquer outorga diretamente relacionada com a regulamentação aplicada, ou qualquer alteração no valor das outorgas após alteração/implementação da regulamentação.",
        "formula": "unitaria",
        "preco_variavel": '{"valor_das_outorgas": 0}',
        "quantidades_json": '{"unitaria": 1}'
    }
]