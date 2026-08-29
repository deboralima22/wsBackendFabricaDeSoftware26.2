# wsBackendFabricaDeSoftware26.2

Projeto de workshop de backend com Django — CRUD de produtos com categoria
relacionada e consumo de API externa (ViaCEP).

## Funcionalidades
- CRUD completo de Produtos
- Relacionamento Produto → Categoria (chave estrangeira)
- Consulta de endereço por CEP via API externa (ViaCEP), com tratamento de erros
- Painel administrativo do Django para gerenciar Categorias

## Como rodar o projeto

\`\`\`bash
git clone <url-do-seu-repositorio>
cd wsBackendFabricaDeSoftware26.2
python -m venv venv
venv\Scripts\activate       # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
\`\`\`

Acesse `http://127.0.0.1:8000/`

## Tecnologias
- Python / Django
- SQLite (banco padrão de desenvolvimento)
- Requests (consumo de API externa)