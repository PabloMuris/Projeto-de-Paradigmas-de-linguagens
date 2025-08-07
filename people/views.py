from django.shortcuts import render
from .mixins import TitleMixin,CurrentUserMixin
# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Curso, Aluno

# Views para Curso

class CursoListView(ListView,TitleMixin):
    title = "Página Inicial"
    model = Curso
    template_name = 'people/courses/course_list.html'

class CursoDetailView(DetailView,TitleMixin):
    title = "Detalhe do curso"
    model = Curso
    template_name = 'people/courses/course_detail.html'

class CursoCreateView(CreateView,TitleMixin,CurrentUserMixin):
    title = "Criar curso"
    model = Curso
    fields = ['nome']
    template_name = 'people/courses/course_form.html'
    success_url = reverse_lazy('curso-list')

class CursoUpdateView(UpdateView,TitleMixin,CurrentUserMixin):
    title = "Modificar Curso"
    model = Curso
    fields = ['nome']
    template_name = 'people/courses/course_form.html'
    success_url = reverse_lazy('curso-list')

class CursoDeleteView(DeleteView,TitleMixin,CurrentUserMixin):
    title = "Deletar curso"
    model = Curso
    template_name = 'people/courses/course_confirm_delete.html'
    success_url = reverse_lazy('curso-list')

# Views para Aluno

class AlunoListView(ListView,TitleMixin):
    title = "Listagem de Alunos"
    model = Aluno
    template_name = 'people/student/student_list.html'

class AlunoDetailView(DetailView,TitleMixin):
    title = "Listagem do Aluno"
    model = Aluno
    template_name = 'people/student/student_detail.html'


class AlunoCreateView(CreateView,TitleMixin,CurrentUserMixin):
    title = "Criar Curso"
    model = Aluno
    fields = ['nome', 'idade', 'curso']
    template_name = 'people/student/student_form.html'
    success_url = reverse_lazy('aluno-list')


class AlunoUpdateView(UpdateView,TitleMixin,CurrentUserMixin):
    title = "Modificar Aluno"
    model = Aluno
    fields = ['nome', 'idade', 'curso']
    template_name = 'people/student/student_form.html'
    success_url = reverse_lazy('aluno-list')

class AlunoDeleteView(DeleteView,TitleMixin):
    title = "Deletar Aluno"
    model = Aluno
    template_name = 'people/student/student_confirm_delete.html'
    success_url = reverse_lazy('aluno-list')


class IndexView(TemplateView,TitleMixin):
    title = "Página inicial"
    template_name = "index.html"