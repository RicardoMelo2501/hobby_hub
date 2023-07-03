# Base para projeto Python/Django

Para Iniciar é recomendando utilizar o venv para instalar os pacotes/modulos necessários para o funcionamento do sistema.

```
pip install venv

# Instanciando o ambiente virtual
python -m venv <nome ambiente>
```

> #### Iniciando Ambiente Virtual

Basta passar o path do arquivo activate

```
# Iniciar
.\<nome ambiente>\Scripts\activate

# Finalizar
deactivate
```

> #### Instalando Módulos / Adionando novos Módulos

Todo e qualquer módulo ou biblioteca adicional criada tem que ser registrada no arquivo requirements.txt

```
pip install -r requirements.txt
```

Comando para criar arquivo de requisitos

```
pip freeze > requirements.txt
```

#### Comando úteis para o Django

Estando num ambiente virtual ou já possuindo todos os requisitos, para rodar o sistema localmente basta digitar:
Comandos Para Apps:

```
# Construir App (Modulos)
python manage.py startapp nome_da_app

```

Comandos Para Models (Fixtures)

```
# Criar migrations (Criar migration baseado no models.py)
python mananage.py makemigrations

# Roda as migrations
python manage.py migrate

# Acessar o Shell
python manage.py shell

# Criando Fixtures (Dados Padrões)
# OBS: O SO importa nessa parte
# Se for Windows Verifique o se o prompt está no padrão utf8
# Usando o CMD
python -Xutf8 manage.py dumpdata --indent 4 app.model > app/fixtures/model.json  && chcp 65001 && type model.json > model.json

```

```
# Criando Super User (/admin)
python manage.py createsuperuser

# Acessar o Shell do Banco de Dados 
python manage.py dbshell

```
