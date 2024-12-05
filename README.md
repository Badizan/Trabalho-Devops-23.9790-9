🚀 Trabalho DevOps - Monitoramento com Prometheus e Grafana
Autor: Leandro Pinecio Malizan
RA: 23.9790-9

📝 Descrição
Este projeto cria e automatiza um ambiente de monitoramento utilizando:
Prometheus: Para coleta de métricas.
Grafana: Para visualização em dashboards.
Jenkins: Para pipeline de integração e deploy.
⚙️ Objetivo: Fornecer um ambiente robusto para monitorar uma aplicação Flask integrada ao banco MariaDB.

📋 Índice
Pré-requisitos
Configuração e Execução
1. Iniciando o Jenkins
2. Criando o Pipeline
3. Executando o Pipeline
4. Rodando sem Jenkins
5. Acessando o Grafana
Estrutura do Pipeline
Dashboard no Grafana
Resumo dos Passos

✅ Pré-requisitos
Certifique-se de que o ambiente possui:
Jenkins instalado e configurado.
Docker e Docker Compose.
Acesso ao navegador.

⚙️ Configuração e Execução
1. Iniciando o Jenkins
Certifique-se de que o Jenkins está rodando em http://localhost:8080.
Faça login com suas credenciais.
2. Criando o Pipeline
No Jenkins, clique em "Nova Tarefa".
Configure como Pipeline e insira:
SCM: Git
Repositório: https://github.com/Badizan/Trabalho-Devops-23.9790-9.
Triggers: H/5 * * * *.


4. Executando o Pipeline
Na tela inicial do Jenkins, selecione o pipeline criado e clique em "Construir Agora".
Monitore os logs e verifique a inicialização dos containers Docker.
5. Rodando sem Jenkins
No terminal, execute o seguinte comando:
docker compose up --build -d

5. Acessando o Grafana
Abra o navegador e acesse: http://localhost:3000.
Faça login:
Usuário: admin
Senha: admin (ou a definida no ambiente).
Ajuste o Time Range para "Last 5 minutes" no dashboard.

📊 Estrutura do Pipeline
O pipeline executa as seguintes etapas:
Clonar Repositório: Baixa o código do GitHub.
Teste: Verifica se o código está funcionando corretamente.
Build: Constrói os containers Docker.
Deploy: Inicializa Prometheus e Grafana.

📈 Dashboard no Grafana
No Grafana, visualize:
Taxas de requisições HTTP.
Conexões no MariaDB.
Métricas do servidor Flask.

🔄 Resumo dos Passos
Configure o Jenkins e o pipeline.
Execute o pipeline ou rode diretamente com Docker Compose.
Acesse e explore as métricas no Grafana.

💡 Observações
Este projeto foi desenvolvido para facilitar a integração de monitoramento em um ambiente automatizado. As instruções são detalhadas para que qualquer desenvolvedor consiga replicar o ambiente
