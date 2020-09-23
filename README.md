# Desafio

Este é um desafio bem próximo dos desafios do dia a dia em projeto em constante evolução feito em python/django.
Ele foi quebrado em algumas etapas. Faça as etapas na ordem que faz mais sentido de acordo com o seu conhecimento.
Você não precisa fazer todas as etapas, mas tente fazer o mais completo possível. Tente garantir que cada
etapa executada seja feita o mais completo possível.

Nestas etapas, vamos sugerir modificações, porem tente manter a estrutura de projeto e fazer testes de integração
quando achar necessário. Se ainda não sabe fazer testes, deixe claro na entrega do seu desafio.

A entrega do desafio deve ser feita com o link do seu repositório de código (pode usar qualquer um que disponibilize um 
visualizador web como por exemplo: bitbucket, github ou gitlab)

## Regras

* Não faça fork desse projeto, copie/utilize o código deste repositório, mas crie um repositório separado para ele.
* Utilize sempre ETAPA referente a mensagem de seus commits
* Fique atendo para não "commitar" arquivos desnecessários
* Foque incialmente em resolver os problemas descritos nas etapas, mas não deixe de dar seu toque especial
para melhorar a solução como um todo.

### Recomendações

* Use o `virtualenv`, fique a vontade para usar o `pipenv` se quiser
* Comentários no código são bem vindos
* Em caso de dúvidas, envie um email.

### Ambiente

* Docker e Docker Compose
* Python 3.8
* Utilize o Pycharm

## Etapa ADMIN

* Criar o admin para os models do app `imovel`
* Neste admin, faça:
    * Um filtro por tipo de imovel
    * Busca pelo nome do imovel
* Criar campos para `criado_em`, `modificado_em` no model de imovel.
* Adicionar no admin uma formar de importar e exportar os dados de cada admin por planilha
    * Procure um projeto para lhe ajudar, não faça do zero

## Etapa LOCALIZACAO

* Adicionar uma nova aplicação chamada `localizacao`
* Com o seguinte model:
    * regiao (slug, nome, estado)
    * cidade (slug, nome, estado, regiao)
* Adicionar uma relação do `imovel` com `regiao`
* Adiciona-los no Admin
* Adiciona-los na API

## Etapa GEOLOCALIZACAO

* Adicionar um campo de `posicao` em propriedade
* Adicionar no admin uma forma de cadastrar esse ponto (dica: `django-leaflet`)
* Crie um endpoint que retorne os imóveis mais proximos de um ponto (lat, long)
* Ordenar estes pontos pela distancia em linha reta do ponto (lat, long) informado.

## Etapa INFRA

* Criar o docker para o projeto
* Adicionar cache para o projeto (dica: `django-cacheops`)
* Preparar o docker-compose para rodar todo o projeto apenas executando `docker-compose up -d`

## Etapa DOCUMENTAÇÃO

* Crie um arquivo de `CHANGELOG.md` explicando o que foi feito em cada etapa executada deixando claro qual foi a ordem de
execução de cada tarefa.
* Marque no readme do projeto que topicos foram feito no `README.md`, e explique o motivo de não ter conseguido fazer
alguma etapa.
* Explique no README o que foi feito alem do que foi solicitado.
