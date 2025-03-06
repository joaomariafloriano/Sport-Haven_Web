from django.urls import path
from .views import FornecedorAPIlistar, FornecedorAPIadicionar, FornecedorAPIatualizar, FornecedorAPIremover

urlpatterns = [
    path('Fornecedor/listar/', FornecedorAPIlistar, name='FornecedorAPIlistar'),
    path('Fornecedor/adicionar/', FornecedorAPIadicionar, name='FornecedorAPIadicionar'),
    path('Fornecedor/atualizar/<int:id>/', FornecedorAPIatualizar, name='FornecedorAPIatualizar'),
    path('Fornecedor/remover/<int:id>/', FornecedorAPIremover, name='FornecedorAPIremover'),
]