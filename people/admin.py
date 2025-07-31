from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Curso, Aluno

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('nome',)
    list_filter = ('is_deleted',)
    ordering = ('nome',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'curso', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('nome',)
    list_filter = ('curso', 'is_deleted')
    ordering = ('nome',)