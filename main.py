import databaseConnect
import zapiConnect

# Função que lista no prompt todos os contatos presentes no banco de dados.
def listAllContacts():
    try:
        db = databaseConnect.dataConnect()
        data = databaseConnect.dataSearch(db, 'contacts')

        for c in data.data:
            print(f'ID: {c['id']} | NOME: {c['Name']} | PHONE: {c['Cellphone']}')
    except:
        print('Erro ao gerar lista de contatos.')

# Função que retorna a lista de todos os contatos presentes no banco de dados.
def getAllContacts():
    try:
        db = databaseConnect.dataConnect()
        data = databaseConnect.dataSearch(db, 'contacts')

        return data.data
    except:
        print('Erro ao adquirir lista de contatos.')

# Função que recebe uma lista de ids de contato retorna a lista de contatos dos ids fornecidos.
def getContactsList(contactList:list):
    db = databaseConnect.dataConnect()
    sendList = []
    for c in contactList:
        data = databaseConnect.dataSearchInTable(db, 'contacts', 'id', c)
        # Realiza uma verificação se data possui um contato em seu conteúdo (se a busca retornou um contato apropriado), caso sim, adiciona o contato a uma lista de envio, caso não, pula o item requerido e mostra uma mensagem de erro em relação ao item.
        if data and data.data:
            sendList.append(data.data[0])# Como data.data é um lista de item único (por ser uma pesquisa por id) optei por capturar o 1º item que é justamente o dicionário do contato.
        else:
            print(f'Erro ao obter contato do cliente de id {c}: falha na conexão ou id inexistente.')
    
    return sendList

# Função que envia saudações para todos os contatos no banco de dados.
def sendGreetingForAll():
    contacts = getAllContacts()
    
    for c in contacts:
        zapiConnect.sendGreeting(c['Name'], c['Cellphone'])

# Nota: sobre as validações de entrada não fiz limpeza de entradas pois o intuito é apenas mostrar de forma mais cadenciada a integração com o banco de dados.

# Função que prende o usuário em um loop até que digite uma entrada valida (s ou n), e ao digitá-la retorna true para s e false para n.
def validInputSN(inputMsg:str):
    while True:
        userInput = input(inputMsg)
        
        if userInput not in 'SNsn' or len(userInput) != 1:
            print('Entrada invalida! Digite apenas S ou N.')
        else:
            if userInput in 'Ss':
                return True
            else:
                return False

# Função que prende o usuário em um loop até que digite uma entrada valida (número inteiro positivo), e retorna a entrada como uma variável int
def validInputPositiveInt(inputMsg):
    while True:
        userInput = input(inputMsg)
        try:
            number = int(userInput)
            if number > 0:
                return number
            print('Entrada invalida! Digite apenas números inteiros maiores que 0.')
        
        except:
            print('Entrada invalida! Digite apenas números inteiros maiores que 0.')




# Execução do Programa
if __name__ == "__main__":
    
    sendAll = validInputSN('Deseja enviar saudações para todos os contatos? (S/N)\n')
    
    if sendAll:
        sendGreetingForAll()
    
    sendSingle = validInputSN('Deseja enviar saudações para contatos específicos? (S/N)\n')

    if sendSingle:
        consultation = validInputSN('Deseja consultar a lista de contatos? (S/N)\n')
        
        while consultation:
            listAllContacts()
            consultation = validInputSN('Deseja consultar a lista de contatos novamente? (S/N)\n')

        numberOfContacts = validInputPositiveInt('Digite a quantidade de contatos para qual deseja enviar saudações:\n')

        idsList = []
        for i in range(0, numberOfContacts):
            contactID = validInputPositiveInt('Digite o número do ID do contato:\n')
            idsList.append(contactID)
        
        contactList = getContactsList(idsList)

        for c in contactList:
            zapiConnect.sendGreeting(c['Name'], c['Cellphone'])
        
    print('Encerrando o programa')