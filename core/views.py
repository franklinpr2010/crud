#apresentar em forma de lista
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Produto


class IndexView(ListView):
    #vai listar produtos
    models = Produto
    #vai criar dentro de index.html
    template_name = 'index.html'
    #consulta que vai trazer todos os produtos
    queryset = Produto.objects.all()
    #nome que vai ser usado para recuperar os dados no template
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    #caso for sucesso redirecionar para o index
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')