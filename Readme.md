# WhatsApp Sender

## Sobre
O WhatsApp Sender é uma aplicação simples em python que visa a automação para envio de mensagens pelo WhatsApp, atravez de uma integração com o Supabase e o Z-API.

## Formato das Variáveis de Ambiente
As variáveis de ambiente devem seguir o seguinte formato no .env:

ZAPI_ID=&lt;&lt;id da instância do Z-API&gt;&gt;

ZAPI_TOKEN=&lt;&lt;token da instância do Z-API&gt;&gt;

ZAPI_CLIENT_TOKEN=&lt;&lt;token de segurança do cliente do Z-API&gt;&gt;

SUPABASE_TOKEN=&lt;&lt;URL do projeto no Supabase&gt;&gt;

SUPABASE_KEY=&lt;&lt;chave de acesso do projeto no Supabase&gt;&gt;

## Formato da Tabela no Banco de Dados
A tabela a qual o programa irá fazer consulta deve ter o nome de 'contacts' e ter os seguintes campos id (chave primaria do tipo int8), Name (do tipo varchar) e Cellphone (do tipo varchar), preencidos respectivamente com a chave identificadora, nome e telefone as pessoas registradas no banco de dados.

**Exemplo:**

### contacts
|id|Name|Cellphone|
|--|----|---------|
|01|Fulano| 5521900000000|
|02|Ciclano| 5521900000001|
|03|Beltrano| 5521900000003|

**NOTA:** o número de celular deve ter o código de país e de área (DDD).

## Como Usar e Como Funciona
No momento a aplicação apenas envia saudações para os contatos registrados (envia uma mensagem de "Olá, &lt;&lt;Nome do Contato&gt;&gt; tudo bem com você?"). Para rodar basta executar o script main.py, irá abrir uma CLI executando a seguinte série de perguntas:

- *"Deseja enviar saudações para todos os contatos? (S/N)"* - caso "s" envia saudações para todos os usuários da tabela e avança para a próxima pergunta, caso "n" apenas avança.
- *"Deseja enviar saudações para contatos específicos? (S/N)"* - caso "s" inicia o processo de seleção dos contatos, caso "n" encerra o programa.
- *"Deseja consultar a lista de contatos? (S/N)"* - caso "s" imprime na tela a lista dos contatos com id, Name e Cellphone e pergunta se deseja consultar novamente a lista (*"Deseja consultar a lista de contatos novamente? (S/N)"*, caso haja algum erro na primeira tentiva), caso "n" avança para a proxima pergunta.
- *"Digite a quantidade de contatos para qual deseja enviar saudações:"* - recebe a quantidade de contatos (número inteiro positivo) para a qual o usuário deseja enviar saldações.
- *"Digite o número do ID do contato:"* - pergunta que se repete pela quantidade de vezes que o usuário informou na quantidade de contatos, e recebe o id numerico do contato (número inteiro positivo) de forma individual. Após isso o programa envia saudações para os contatos com os respectivos ids informados.

Ao término o programa exibe a mensagem de enceramento.



*Demais informações estão comentadas no código.*
