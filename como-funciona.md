<h3>
## Componentes e Etapas:
</h3>
Usuários: Representam os clientes ou sistemas externos que acessam a API para realizar operações (como criar, listar ou deletar clientes).

API Gateway: Atua como uma camada intermediária, recebendo as requisições HTTP dos usuários e direcionando-as ao cluster ECS. Ele também pode aplicar políticas de segurança, como autenticação e autorização.

ECS Cluster (Elastic Container Service): Aqui é onde os containers Docker que executam a aplicação FastAPI estão rodando. Cada container recebe as requisições da API Gateway e processa a lógica de negócio, como ler ou escrever dados no banco de dados.

Banco de Dados RDS (PostgreSQL): Armazena os dados dos clientes. O ECS Cluster se conecta ao RDS para ler e gravar dados de clientes.

Fluxo de Dados: As setas no diagrama indicam o caminho que as requisições percorrem. Os usuários fazem uma requisição -> a API Gateway a recebe e envia ao ECS Cluster -> o cluster consulta ou altera os dados no banco PostgreSQL -> a resposta é enviada de volta para o usuário.
