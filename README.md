# E-Shopping

## Descrição:

Nesse projeto realizado em equipe foi desenvolvido uma aplicação backend voltada para a estruturação de uma api de marketplace,com o objetivo de facilitar o usuário a cadastrar sua empresa de uma maneira simples e dinâmica no site da sua empresa, com o auxílio de regras de negócios que deixam a aplicação mais segura e eficaz.
A aplicação contou com a utilização de bibliotecas como a do mercadopago e gerencianet para o desenvolvimento da funcionalidade de pagamento.

## Regras de negócio utilizadas na aplicação:

- A obtenção do acesso para que um usuário possa cadastrar sua empresa é através de uma permissão concedida por algum dos administradores da aplicação.
- Cadastramento de categorias de produtos e os produtos serão feitos apenas pelas empresas cadastradas na aplicação.
- Usuários apenas poderão prosseguir com produtos para o carrinho, com suas contas de usuários logadas e autenticadas.
- Apenas usuários admin têm privilégios nos acessos das rotas da aplicação. 

## Link deploy da aplicação:

- https://e-commerce-api-m0va.onrender.com/

### Para inicializar a aplicação (local):

````
python manage.py runserver
````

## Tecnologias utilizadas:

- black
- click
- dj-database-url
- Django
- django-environ
- django-formtools
- django-otp
- django-phonenumber-field
- django-registration
- django-rest-swagger
- django-softdelete
- django-two-factor-auth
- djangorestframework
- djangorestframework-simplejwt
- drf-spectacular
- environ
- executing
- gerencianet
- gunicorn
- ipdb
- ipython
- itypes
- jedi
- jsonschema
- MarkupSafe
- matplotlib-inline
- mercadopago
- psycopg2-binary
- pycodestyle
- pycryptodome
- PyJWT
- PyQRCode
- pyrsistent
- pytest
- pytest-django
- pytest-testdox
- qrcode
- simplejson
- sqlparse
- stack-data
- uritemplate
- urllib3

## Diagrama da aplicação:

![Diagrama EShopping](https://user-images.githubusercontent.com/96259892/212782437-4f8ba1cf-1efb-45fc-85d1-e5fd6074d040.png)

## Fluxograma da aplicação:

![fluxo grama E-Shopping](https://user-images.githubusercontent.com/96259892/212782222-3e5a728a-d11f-4899-aa14-ba1176bc475f.png)
