class TitleMixin:
    title = None  

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context
    
class CurrentUserMixin:
    """
    Mixin para views genéricas do Django que preenche automaticamente
    os campos 'created_by' e 'updated_by' com o usuário autenticado.

    Este mixin assume que a view está sendo usada com um formulário
    que corresponde a um modelo que herda de CreationTimestampedModel
    e/ou UpdateTimestampedModel, e que o request.user está disponível.
    """

    def form_valid(self, form):
        """
        Sobrescreve o método form_valid para adicionar o usuário antes de salvar o objeto.
        """
        # Pega a instância do modelo, mas não salva no banco de dados ainda.
        instance = form.save(commit=False)

        # Se for um objeto novo (criação), define o criador.
        # Verifica se o campo 'created_by' existe no modelo da instância.
        if instance.pk is None and hasattr(instance, 'created_by'):
            instance.created_by = self.request.user
        
        # Se for um objeto existente (atualização), define o atualizador.
        # Verifica se o campo 'updated_by' existe no modelo da instância.
        if instance.pk is not None and hasattr(instance, 'updated_by'):
            instance.updated_by = self.request.user
        
        # Salva o objeto no banco de dados.
        instance.save()
        
        # Opcional: salva os Many-to-Many se houver
        form.save_m2m()

        return super().form_valid(form)