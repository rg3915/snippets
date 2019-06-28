# models.py
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import *


class Person(models.Model):
    firstname = models.CharField(_('Nome'), max_length=20)
    objects = PersonManager()

    def __str__(self):
        return self.firstname

# managers.py

from django.db import models


class PersonManager(models.Manager):

    def search_person(self, person):
        return self.filter(firstname__contains=person)

# manage shell

from myproject.core.models import Person
p = Person.objects.search_person('James')
p
p.count()
