Deploy da Aplicação FastAPI
Este documento descreve o processo de deploy da aplicação FastAPI utilizando o Amazon ECS (Elastic Container Service) e GitHub Actions. O deploy automatizado permite que você envie alterações de código para o ambiente de produção de forma eficiente e confiável.

Pré-requisitos
Antes de iniciar o processo de deploy, certifique-se de que você possui os seguintes itens configurados:

Uma conta AWS com acesso ao Amazon ECS e ECR (Elastic Container Registry).
Um repositório Git com o código da sua aplicação.
AWS CLI configurada em seu ambiente local (opcional, mas recomendado para testes).
Estrutura do Projeto
Certifique-se de que a estrutura do seu projeto esteja organizada conforme o esperado:

bash
Copiar código
/seu-projeto
│
├── .github/
│   └── workflows/
│       └── deploy.yml  # Workflow do GitHub Actions para deploy
│
├── app/
│   └── main.py          # Código da aplicação FastAPI
│
├── requirements.txt      # Dependências do projeto
│
└── Dockerfile            # Dockerfile para construção da imagem
Configuração do GitHub Actions
Criar o Workflow de Deploy
Crie um arquivo chamado deploy.yml no diretório .github/workflows/ do seu repositório com o seguinte conteúdo:
yaml
Copiar código
name: Deploy to AWS

on:
  push:
    branches:
      - main  # Ou sua branch principal

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Build Docker image
      run: docker build -t itauapi2-fastapi .

    - name: Log in to Amazon ECR
      run: |
        aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com

    - name: Tag Docker image
      run: docker tag itauapi2-fastapi:latest your-account-id.dkr.ecr.your-region.amazonaws.com/itauapi2-fastapi:latest

    - name: Push Docker image
      run: docker push your-account-id.dkr.ecr.your-region.amazonaws.com/itauapi2-fastapi:latest

    - name: Deploy to ECS
      run: |
        aws ecs update-service --cluster your-cluster-name --service your-service-name --force-new-deployment
Realizando o Deploy
Fazendo um Push para o Repositório

Após realizar alterações no código ou na configuração da aplicação, faça um push das suas alterações para a branch principal do repositório. Isso acionará automaticamente o workflow de deploy configurado no GitHub Actions.
Monitorando o Processo de Deploy

Acesse a aba Actions no seu repositório GitHub para monitorar a execução do workflow. Você poderá ver logs detalhados de cada etapa do processo de build e deploy.
Verificando o Deploy

Acesse o console do AWS e verifique se o serviço ECS foi atualizado corretamente com a nova imagem. Você pode visualizar a tarefa e o estado do serviço na interface do ECS.
Testando a API
Após o deploy, você pode testar a API utilizando várias ferramentas. Aqui estão algumas sugestões:

Obtenha o Endpoint da API
No console do AWS, encontre o Load Balancer associado ao seu serviço ECS. Anote o DNS name.
Testes com cURL
Utilize o curl para fazer requisições à sua API:
bash
Copiar código
# Teste o endpoint raiz
curl http://<your-load-balancer-dns>:80/

# Teste um endpoint específico (exemplo: listando clientes)
curl http://<your-load-balancer-dns>:80/clients
Testes com Postman
Abra o Postman e crie uma nova requisição.
Insira a URL da sua API (por exemplo, http://<your-load-balancer-dns>:80/clients).
Configure o método HTTP (GET, POST, etc.) e adicione cabeçalhos ou corpo da requisição conforme necessário.
Clique em Send para visualizar a resposta.
Monitoramento e Logs
Utilize o AWS CloudWatch para monitorar logs e métricas da sua aplicação. Isso ajudará a identificar quaisquer problemas ou anomalias na operação da API.
