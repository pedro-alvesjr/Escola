"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from sistema.views import lista_alunos, detalhes_aluno, registrar_falta, marcar_reposicao_ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_alunos, name='lista_alunos'),
    path('aluno/<int:aluno_id>/', detalhes_aluno, name='detalhes_aluno'),
    path('aluno/<int:aluno_id>/registrar_falta/', registrar_falta, name='registrar_falta'),
    path('falta/<int:falta_id>/marcar_reposicao/', marcar_reposicao_ajax, name='marcar_reposicao'),
    path('', include('sistema.urls')),  # Inclui as URLs do app sistema
]
