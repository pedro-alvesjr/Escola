from django.urls import path
from .views import lista_alunos, detalhes_aluno, registrar_falta, marcar_reposicao_ajax

urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path('aluno/<int:aluno_id>/', detalhes_aluno, name='detalhes_aluno'),
    path('aluno/<int:aluno_id>/registrar_falta/', registrar_falta, name='registrar_falta'),
    path('falta/<int:falta_id>/reposicao_ajax/', marcar_reposicao_ajax, name='marcar_reposicao_ajax'),

]