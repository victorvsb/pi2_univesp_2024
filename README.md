# pi2_univesp_2024
Repositório para o PI-2 da UNIVESP - Grupo DRP03-PJI240-SALA-003GRUPO-015


O objetivo do projeto é incrementar as funcionalidades presentes da versão desenvolvida no PI-1.

## Fazer download do projeto
`git clone https://github.com/victorvsb/pi2_univesp_2024`

## Criar o ambiente virtual e instalar requirements.txt

`python -m venv venv`

-`venv/Script/activate`

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

## Criar o Banco de Dados
`python manage.py migrate`

## Criar o Usuário admin
`python manage.py createsuperuser`

## Carregar dados iniciais
`python.exe .\manage.py loaddata .\fixtures\dados_completos.json`

## Outros comandos

Atualizar o arquivo requirements.txt
`pip freeze > requirements.txt`

Para criar a fixture com os dados:
`python -Xutf8 .\manage.py dumpdata app_gerenciador --indent 2 -o .\fixtures\dados_completos.json`

`python -Xutf8 .\manage.py dumpdata app_gerenciador.material --indent 2 -o .\fixtures\material.json`
