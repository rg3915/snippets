# Criando comandos personalizados

https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/
https://django-document-tchinese.readthedocs.org/en/stable-1.3.x/howto/custom-management-commands.html

Sintaxe:

	myapp/__init__.py
	myapp/management/__init__.py
	myapp/management/commands/__init__.py
	myapp/management/commands/icreclameaquiapi.py

Exemplo:

	mkdir -p core/management/commands
	touch core/management/__init__.py
	touch core/management/commands/__init__.py
	touch core/management/commands/entradas.py


	python manage.py entradas
