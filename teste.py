from database.models.subcategoria import SubCategoria

for sub in SubCategoria.select():
    if not sub.tipo_preco:  # Se estiver vazio ou None
        sub.tipo_preco = "valor padrão"  # Insira um valor padrão
        sub.save()