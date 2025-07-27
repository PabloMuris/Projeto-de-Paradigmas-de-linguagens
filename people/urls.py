from django.urls import path
from .views import (
    CursoListView, CursoDetailView, CursoCreateView, CursoUpdateView, CursoDeleteView,
    AlunoListView, AlunoDetailView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView
)

urlpatterns = [
    # URLs de Curso
    path('cursos/', CursoListView.as_view(), name='curso-list'),
    path('cursos/novo/', CursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('cursos/<int:pk>/editar/', CursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/excluir/', CursoDeleteView.as_view(), name='curso-delete'),

    # URLs de Aluno
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/novo/', AlunoCreateView.as_view(), name='aluno-create'),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
    path('alunos/<int:pk>/editar/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('alunos/<int:pk>/excluir/', AlunoDeleteView.as_view(), name='aluno-delete'),
]
