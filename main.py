import databaseConnect
import zapiConnect

def listContacts():
    try:
        db = databaseConnect.dataConnect()
        data = databaseConnect.dataSearch(db, 'contacts')

        for c in data.data:
            print(f'ID: {c['id']} | NOME: {c['Name']} | PHONE: {c['Cellphone']}')
    except:
        print('Erro ao gerar lista de contatos.')

def getAllContacts():
    try:
        db = databaseConnect.dataConnect()
        data = databaseConnect.dataSearch(db, 'contacts')

        return data.data
    except:
        print('Erro ao adquirir lista de contatos.')

def getContactsList(contactList:list):
    db = databaseConnect.dataConnect()
    data = databaseConnect.dataSearchInTable(db, 'contacts', 'id', contactList)

def sendGreeting(name:str, phone:str):
    message = f'Olá, {name} tudo bem com você?'
    try:
        zapiConnect.sendMessage(phone, message)
    except:
        print('Erro ao enviar saudação.')        

def sendGreetingForAll():
    contacts = getAllContacts()
    
    for c in contacts:
        sendGreeting(c['Name'], c['Cellphone'])

if __name__ == "__main__":
    listContacts()
    
