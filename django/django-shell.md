Manipulando [timezones](https://docs.djangoproject.com/en/1.9/topics/i18n/timezones/).

```python
>>> import datetime
>>> import pytz
>>> from django.utils import timezone
>>> for i in pytz.all_timezones:
...     print(i)
... 
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
Africa/Asmara
Africa/Asmera
Africa/Bamako
...
```

## CRUD

Inserindo data

```python
>>> from djexperience.bookstore.models import Customer, Author, Book
>>> saopaulo_tz = pytz.timezone('America/Sao_Paulo')
>>> d = saopaulo_tz.localize(datetime.datetime(1815, 12, 10, 23, 59, 59, 654000))
>>> d
datetime.datetime(1815, 12, 10, 23, 59, 59, 654000, tzinfo=<DstTzInfo 'America/Sao_Paulo' LMT-1 day, 20:54:00 STD>)
```

### Create

```python
>>> customer = Customer(first_name='Ada', last_name='Lovelace', email='ada@example.com', birthday=d)
>>> customer.save()
```

Usando o método `create`

```python
>>> data_atual = saopaulo_tz.localize(datetime.datetime.now())
>>> Customer.objects.create(first_name='Edward', last_name='Snowden', email='snowden@example.com', birthday=data_atual)
<Customer: Edward>
```

Timezone atual

```python
>>> t = timezone.now()
>>> Customer.objects.create(first_name='John', last_name='Smith', email='js@example.com', birthday=t)
<Customer: John>
```

Criando mais registros

```python
>>> d = saopaulo_tz.localize(datetime.datetime(1956, 1, 31, 0, 0, 0, 654000))
>>> Customer.objects.create(first_name='Guido', last_name='van Rossum', email='guido@example.com', birthday=d)
<Customer: Guido>
>>> t = timezone.now()
>>> Customer.objects.create(first_name='Jacob', last_name='Kaplan-Moss', email='jkm@example.com', birthday=t)
<Customer: Jacob>
```

### Read

```python
>>> customers = Customer.objects.all()
>>> customers
[<Customer: Ada>, <Customer: Edward>, <Customer: Guido>, <Customer: Jacob>, <Customer: John>]
```

### Filtrando

```python
>>> Customer.objects.filter(birthday__year=2016)
[<Customer: Edward>, <Customer: Jacob>, <Customer: John>]
```

### Contando

```python
>>> Customer.objects.filter(birthday__year=2016).count()
3
>>> Customer.objects.filter(birthday__year__lte=2000).count()
2
```

### Update

```python
>>> Customer.objects.filter(birthday__year__lte=2000).update(active=False)
2
```

[BasicComparisonFilters](https://code.djangoproject.com/wiki/BasicComparisonFilters)

### Delete

Deletando com `filter`

```python
>>> Customer.objects.filter(id=1).delete()
(2, {'bookstore.People': 1, 'bookstore.Customer': 1})
```

Deletando com `get`

```python
>>> c = Customer.objects.get(pk=2)
>>> c.delete()
(2, {'bookstore.People': 1, 'bookstore.Customer': 1})
```

**Cuidado** pra não deletar tudo

```python
>>> Customer.objects.all().delete()
(6, {'bookstore.People': 3, 'bookstore.Customer': 3})
```


### Explorando um pouco mais

Vamos inserir registros novamente

```python
saopaulo_tz = pytz.timezone('America/Sao_Paulo')
d = saopaulo_tz.localize(datetime.datetime(1815, 12, 10, 23, 59, 59, 654000))
Customer.objects.create(first_name='Ada', last_name='Lovelace', email='ada@example.com', birthday=d)
data_atual = saopaulo_tz.localize(datetime.datetime.now())
Customer.objects.create(first_name='Edward', last_name='Snowden', email='snowden@example.com', birthday=data_atual)
t = timezone.now()
Customer.objects.create(first_name='John', last_name='Smith', email='js@example.com', birthday=t)
d = saopaulo_tz.localize(datetime.datetime(1956, 1, 31, 0, 0, 0, 654000))
Customer.objects.create(first_name='Guido', last_name='van Rossum', email='guido@example.com', birthday=d)
t = timezone.now()
Customer.objects.create(first_name='Jacob', last_name='Kaplan-Moss', email='jkm@example.com', birthday=t)
```

Visualizando o primeiro elemento

```python
>>> customers = Customer.objects.all()[0]
>>> customers.email
'ada@example.com'
>>> customers.birthday
datetime.datetime(1815, 12, 11, 3, 5, 59, 654000, tzinfo=<UTC>)
```

Visualizando alguns campos

```python
>>> customers = Customer.objects.all()
>>> for i in customers:
...     print(i.email, i.birthday, i.active)
... 
ada@example.com 1815-12-11 03:05:59.654000+00:00 True
snowden@example.com 2016-05-30 03:06:40.846590+00:00 True
guido@example.com 1956-01-31 03:00:00.654000+00:00 True
jkm@example.com 2016-05-30 03:06:41.439811+00:00 True
js@example.com 2016-05-30 03:06:41.041260+00:00 True
```

Definindo uma ordem

```python
>>> customers = Customer.objects.all().order_by('active')
>>> for i in customers:
...     print(i.first_name, i.birthday, i.active)
... 
Ada 1815-12-11 03:05:59.654000+00:00 True
Edward 2016-05-30 03:06:40.846590+00:00 True
John 2016-05-30 03:06:41.041260+00:00 True
Guido 1956-01-31 03:00:00.654000+00:00 True
Jacob 2016-05-30 03:06:41.439811+00:00 True
```

### Listas

```python
>>> customers = Customer.objects.all().values_list()
>>> for i in customers:
...     print(i)
... 
(13, 'Ada', 'Lovelace', 'ada@example.com', datetime.datetime(1815, 12, 11, 3, 5, 59, 654000, tzinfo=<UTC>), True, 13)
(14, 'Edward', 'Snowden', 'snowden@example.com', datetime.datetime(2016, 5, 30, 3, 6, 40, 846590, tzinfo=<UTC>), True, 14)
(16, 'Guido', 'van Rossum', 'guido@example.com', datetime.datetime(1956, 1, 31, 3, 0, 0, 654000, tzinfo=<UTC>), True, 16)
(17, 'Jacob', 'Kaplan-Moss', 'jkm@example.com', datetime.datetime(2016, 5, 30, 3, 6, 41, 439811, tzinfo=<UTC>), True, 17)
(15, 'John', 'Smith', 'js@example.com', datetime.datetime(2016, 5, 30, 3, 6, 41, 41260, tzinfo=<UTC>), True, 15)
```

### Dicionários

```python
>>> customers = Customer.objects.all().values()
>>> for i in customers:
...     print(i)
... 
{'last_name': 'Lovelace', 'active': True, 'people_ptr_id': 13, 'birthday': datetime.datetime(1815, 12, 11, 3, 5, 59, 654000, tzinfo=<UTC>), 'email': 'ada@example.com', 'first_name': 'Ada', 'id': 13}
{'last_name': 'Snowden', 'active': True, 'people_ptr_id': 14, 'birthday': datetime.datetime(2016, 5, 30, 3, 6, 40, 846590, tzinfo=<UTC>), 'email': 'snowden@example.com', 'first_name': 'Edward', 'id': 14}
{'last_name': 'van Rossum', 'active': True, 'people_ptr_id': 16, 'birthday': datetime.datetime(1956, 1, 31, 3, 0, 0, 654000, tzinfo=<UTC>), 'email': 'guido@example.com', 'first_name': 'Guido', 'id': 16}
{'last_name': 'Kaplan-Moss', 'active': True, 'people_ptr_id': 17, 'birthday': datetime.datetime(2016, 5, 30, 3, 6, 41, 439811, tzinfo=<UTC>), 'email': 'jkm@example.com', 'first_name': 'Jacob', 'id': 17}
{'last_name': 'Smith', 'active': True, 'people_ptr_id': 15, 'birthday': datetime.datetime(2016, 5, 30, 3, 6, 41, 41260, tzinfo=<UTC>), 'email': 'js@example.com', 'first_name': 'John', 'id': 15}
```

```python
>>> customers = Customer.objects.all().values('first_name', 'email', 'active').order_by('active')
>>> for i in customers:
...     print(i)
... 
{'email': 'ada@example.com', 'active': True, 'first_name': 'Ada'}
{'email': 'snowden@example.com', 'active': True, 'first_name': 'Edward'}
{'email': 'js@example.com', 'active': True, 'first_name': 'John'}
{'email': 'guido@example.com', 'active': True, 'first_name': 'Guido'}
{'email': 'jkm@example.com', 'active': True, 'first_name': 'Jacob'}
```

Visualizando o nome dos campos

```python
>>> [x for x in Customer().__dict__.keys() if not x.startswith('_')]
['last_name', 'active', 'people_ptr_id', 'birthday', 'email', 'first_name', 'id']
```

Criando vários registros de uma vez.

```python
>>> AUTHOR_LIST = (
...     'Antoine de Saint - Exupéry',
...     'Isabela Freitas',
...     'John Green',
...     'Bela Gil',
...     'Jeff Kinney',
... )
>>> 
>>> obj = [Author(name=v) for v in AUTHOR_LIST]
>>> Author.objects.bulk_create(obj)
[<Author: Antoine de Saint - Exupéry>, <Author: Isabela Freitas>, <Author: John Green>, <Author: Bela Gil>, <Author: Jeff Kinney>]
>>> Author.objects.all().count()
5
```


## Vendo o SQL equivalente de uma consulta do Django

Se no Django fazemos uma consulta do tipo

```python
>>> from djexperience.bookstore.models import Author
>>> consulta = Author.objects.all()
```

para ver o equivalente em SQl basta digitar

```python
>>> print(consulta.query)
SELECT "bookstore_author"."id", "bookstore_author"."name" FROM "bookstore_author" ORDER BY "bookstore_author"."name" ASC
```


## Aggregate

### Aggregate

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur eligendi, explicabo sunt maxime cum facere excepturi magnam ad, quas dignissimos rerum quidem eum consectetur similique, libero placeat architecto voluptatibus ab!

### Annotate

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nemo eaque, laborum ratione, explicabo odit placeat pariatur laudantium, quae facere tenetur atque id expedita fuga. Consectetur esse deserunt vero mollitia sunt!


http://blog.roseman.org.uk/2010/05/10/django-aggregation-and-simple-group/

http://henriquebastos.net/agregacoes-condicionais-com-django-aggregate-if/
