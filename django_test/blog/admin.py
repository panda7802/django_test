from django.contrib import admin

from blog.models import Person
from blog.models import UserForm

# Register your models here.
admin.site.register(Person)
admin.site.register(UserForm)