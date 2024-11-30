import os
from peewee import SqliteDatabase, PostgresqlDatabase
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# db = SqliteDatabase('calculadora.db')

# Configura o banco de dados
db = PostgresqlDatabase(
    os.getenv('DB_NAME'),       # Nome do banco
    user=os.getenv('DB_USER'),  # Usuário
    password=os.getenv('DB_PASSWORD'),  # Senha
    host=os.getenv('DB_HOST'),  # Endpoint
    port=int(os.getenv('DB_PORT')),  # Porta
    sslmode=os.getenv('DB_SSLMODE'),  # SSL Mode
    sslrootcert=os.getenv('DB_SSLROOTCERT')  # Caminho do certificado SSL
)

try:
    db.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")
finally:
    db.close()