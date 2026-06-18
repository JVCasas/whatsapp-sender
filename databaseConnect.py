import os
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv('SUPABASE_TOKEN')
key: str = os.getenv('SUPABASE_KEY')

# Função que cria uma conexão com o Supabase, retorna um objeto cliente do Supabase
def dataConnect():

    supabaseClient: Client = create_client(url, key)

    return supabaseClient

# Função que recebe um cliente Supabase e o nome de uma tabela e retorna um objeto de pesquisa com a tabela informada, retorna uma lista vazia em caso de erro.
def dataSearch(database: Client, tableName: str):
    try:
        searchRequest = database.table(tableName).select('*').execute()

        return searchRequest
    
    except Exception as e:
        print(f'Erro ao buscar no banco de dados: {e}')
        
        return []

# Função que pesquisa por itens especificos em uma tabela, recebe um cliente Supabase, o nome de uma tabela, o nome de uma coluna dessa tabela e um valor a ser pesquisado, retorna um objeto de pesquisa com o item desejado, retorna uma lista vazia em caso de erro.
def dataSearchInTable(database: Client, tableName: str, collumn:str, value):

    try:
        searchRequest = database.table(tableName).select('*').eq(collumn, value).execute()

        return searchRequest
    
    except Exception as e:
        print(f'Erro ao buscar no banco de dados: {e}')
        
        return []