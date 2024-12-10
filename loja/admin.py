from django.contrib import admin  
from .models import Usuario, Loja, Produto, Fornecedor, Cliente, Pedido, NotaFiscal, MetodoDePagamento, ItemPedido  

class UsuarioAdmin(admin.ModelAdmin):  
    list_display = ('nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'foto')  

class LojaAdmin(admin.ModelAdmin):  
    list_display = ('cnpj', 'nome', 'email', 'telefone', 'endereco',)   

class ProdutoAdmin(admin.ModelAdmin):  
    list_display = ('nome', 'preco', 'descricao', 'quantidadeEstoque', 'foto')  

class FornecedorAdmin(admin.ModelAdmin):  
    list_display = ('cnpj', 'nome','telefone', 'email', 'endereco')  

class ClienteAdmin(admin.ModelAdmin):  
    list_display = ('nome', 'cpf', 'telefone', 'email')  

class PedidoAdmin(admin.ModelAdmin):  
    list_display = ('dataPedido', 'valorTotal', 'enderecoEntrega', 'metodoDePagamento')  

class NotaFiscalAdmin(admin.ModelAdmin):  
    list_display = ('dataEmissao', 'informacoesCliente')  

class MetodoDePagamentoAdmin(admin.ModelAdmin):  
    list_display = ('descricaoPagamento', 'tipoPagamento')  

class ItemPedidoAdmin(admin.ModelAdmin):  
    list_display = ('quantidade', 'precoUnitario')  

admin.site.register(Usuario, UsuarioAdmin)  
admin.site.register(Loja, LojaAdmin)  
admin.site.register(Produto, ProdutoAdmin)  
admin.site.register(Fornecedor, FornecedorAdmin)  
admin.site.register(Cliente, ClienteAdmin)  
admin.site.register(Pedido, PedidoAdmin)  
admin.site.register(NotaFiscal, NotaFiscalAdmin)  
admin.site.register(MetodoDePagamento, MetodoDePagamentoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)