from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Falta
from django.http import JsonResponse


# Lista todos os alunos
def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')  # Ordena alfabeticamente
    return render(request, 'sistema/lista_alunos.html', {'alunos': alunos})

# Exibe as faltas de um aluno específico
def detalhes_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    faltas = Falta.objects.filter(aluno=aluno).order_by('-data_falta')
    return render(request, 'sistema/detalhes_aluno.html', {'aluno': aluno, 'faltas': faltas})

# Registra uma nova falta
def registrar_falta(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == 'POST':
        data_falta = request.POST.get('data_falta')
        Falta.objects.create(aluno=aluno, data_falta=data_falta)
        return redirect('detalhes_aluno', aluno_id=aluno.id)
    return render(request, 'sistema/registrar_falta.html', {'aluno': aluno})

# Marca uma falta como "Reposição Feita"
def marcar_reposicao_ajax(request, falta_id):
    falta = get_object_or_404(Falta, id=falta_id)
    falta.respondida = True  # Corrigido para usar o campo correto
    falta.save()
    return JsonResponse({'status': 'success', 'respondida': falta.respondida})

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário", widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
