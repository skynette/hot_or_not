from django.contrib import admin
from .models import Person, Hotvote, Notvote

# Register your models here.
admin.site.register(Person)
admin.site.register(Hotvote)
admin.site.register(Notvote)