# pi2_univesp_2024
Repositório para o PI-2 da UNIVESP - Grupo DRP03-PJI240-SALA-003GRUPO-015


O objetivo do projeto é incrementar as funcionalidades presentes da versão desenvolvida no PI-1.

## Fazer download do projeto
git checkout 

## Criar o Banco de Dados
`python manage.py migrate`


## Criar o Usuário admin
`python manage.py createsuperuser`

## Exportar dados

Para criar a fixture com os dados:

`python -Xutf8 .\manage.py dumpdata app_gerenciador --indent 2 -o .\fixtures\teste.json`

Para carregar a fixture criada:

`python.exe .\manage.py loaddata .\fixtures\teste.json`
