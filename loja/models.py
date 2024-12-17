from django.db import models

#Teste Model


class SavedItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#Fim teste Model

class Usuario(models.Model):  
    nome = models.CharField('Nome', max_length=100)  
    sobrenome = models.CharField('Sobrenome', max_length=100, blank=True)  
    cpf = models.CharField('CPF', max_length=14, unique=True)           # O CPF terá 14 caracteres no formato "000.000.000-00"
    telefone = models.CharField('Telefone', max_length=15, blank=True)  # O telefone terá 15 caracteres no formato "(00) 00000-0000" 
    email = models.EmailField('Email', max_length=100, unique=True)  
    endereco = models.TextField('Endereço', max_length=500, null=True)
    foto = models.ImageField('Foto do Usuário', upload_to='usuarios/', blank=True)  

    class Meta:
        permissions = [
            ("permissao_01", "Poderá acessar a view da pagina_1.html"),
            ("permissao_02", "Poderá visualizar um texto do template")
        ]

    def __str__(self):  
        return f'{self.nome} {self.sobrenome}'  

class Loja(models.Model):  
    cnpj = models.CharField('CNPJ', max_length=14, unique=True)  
    nome = models.CharField('Nome da Loja', max_length=100)  
    email = models.EmailField('Email', unique=True)  
    telefone = models.CharField('Telefone', max_length=15, blank=True)  
    endereco = models.TextField('Endereço', max_length=500)  

    def __str__(self):  
        return self.nome  

class Produto(models.Model):  
    nome = models.CharField('Nome do Produto', max_length=100)  
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)  
    descricao = models.TextField('Descrição', blank=True)  
    quantidadeEstoque = models.IntegerField('Quantidade em Estoque', default=0)  
    foto = models.ImageField('Foto do Produto', upload_to='produtos/', blank=True)  
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.nome  

class Fornecedor(models.Model):  
    cnpj = models.CharField('CNPJ', max_length=15, unique=True)  
    nome = models.CharField('Nome do Fornecedor', max_length=100)  
    telefone = models.CharField('Telefone', max_length=15, blank=True)  
    email = models.EmailField('Email', max_length=100, blank=True)
    endereco = models.TextField('Endereço', max_length=500)  

    def __str__(self):  
        return self.nome  

class Cliente(models.Model):  
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE) 
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)  
    telefone = models.CharField('Telefone', max_length=15)  
    email = models.EmailField('Email', max_length=255) 

    def __str__(self):  
        return f'{self.usuario.nome} {self.usuario.sobrenome}'  


class MetodoDePagamento(models.Model):  
    descricaoPagamento = models.CharField('Descrição do Pagamento', max_length=255)  
    tipoPagamento = models.CharField('Tipo do Pagamento', max_length=50)  

    def __str__(self):  
        return self.descricaoPagamento  
    
class Pedido(models.Model):  
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  
    metodoDePagamento = models.ForeignKey(MetodoDePagamento, on_delete=models.CASCADE, null=True)  

    dataPedido = models.DateTimeField('Data do Pedido', auto_now_add=True, editable=False)
    valorTotal = models.DecimalField('Valor Total', max_digits=15, decimal_places=2)
    enderecoEntrega = models.TextField('Endereço de Entrega', max_length=500)
    # metodoPagamento = models.CharField('Método de Pagamento', max_length=50) 

    def __str__(self):  
        return f'Pedido {self.id} - {self.cliente.usuario.nome}'  

class NotaFiscal(models.Model):  
    dataEmissao = models.DateField('Data de Emissão', auto_now_add=True)  
    informacoesCliente = models.TextField('Informações do Cliente', max_length=500)  
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  

    def __str__(self):  
        return f'Nota Fiscal {self.id} - Pedido {self.pedido.id}'
    
class ItemPedido(models.Model):  
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Supondo que existe um modelo Produto  
    quantidade = models.PositiveIntegerField('Quantidade')  
    precoUnitario = models.DecimalField('Preço Unitário', max_digits=15, decimal_places=2)