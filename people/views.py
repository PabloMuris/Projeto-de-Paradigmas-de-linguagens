from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Curso, Aluno

# Views para Curso

class CursoListView(ListView):
    model = Curso
    template_name = 'people/courses/course_list.html'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'people/courses/course_detail.html'

class CursoCreateView(CreateView):
    model = Curso
    fields = ['nome']
    template_name = 'people/courses/course_form.html'
    success_url = reverse_lazy('curso-list')

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nome']
    template_name = 'people/courses/course_form.html'
    success_url = reverse_lazy('curso-list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'people/courses/course_confirm_delete.html'
    success_url = reverse_lazy('curso-list')

# Views para Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'people/student/student_list.html'

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'people/student/student_detail.html'

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome', 'idade', 'curso']
    template_name = 'people/student/student_form.html'
    success_url = reverse_lazy('aluno-list')

class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ['nome', 'idade', 'curso']
    template_name = 'people/student/student_form.html'
    success_url = reverse_lazy('aluno-list')

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'people/student/student_confirm_delete.html'
    success_url = reverse_lazy('aluno-list')
