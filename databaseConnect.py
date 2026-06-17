import os
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv('SUPABASE_TOKEN')
key: str = os.getenv('SUPABASE_KEY')

def dataConnect() -> Client:

    supabaseClient: Client = create_client(url, key)

    return supabaseClient


def dataSearch(database: Client, tableName: str) -> list[dict]:
    try:
        searchRequest = database.table(tableName).select('*').execute()

        return searchRequest
    
    except Exception as e:
        print(f'Erro ao buscar no banco de dados: {e}')
        
        return []
