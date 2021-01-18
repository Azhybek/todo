from django.contrib import admin
from .models import ToDo
from .models import ToDo, book

admin.site.register(ToDo)
admin.site.register(book)
