from django.contrib import admin
from django.contrib import admin
from .models import Aluno, Falta

# Registra os modelos para aparecerem no painel admin
admin.site.register(Aluno)
admin.site.register(Falta)
