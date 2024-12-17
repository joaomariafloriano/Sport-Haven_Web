from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Usuario, Produto, Fornecedor, SavedItem
from .forms import UsuarioForm, ProdutoForm, FornecedorForm, SavedItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User     # Adicionado, para a classe usuário do django
from django.contrib import messages             # Adicionado para alerts
from django.contrib.messages import constants   # Adicionado para alerts
from django.contrib import auth                 # Adicionado, para autenticação
from django.contrib.auth.decorators import permission_required

def home(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'home.html', {'user_name': user_name})

#Testando Views

def saved_items_view(request):
    items = SavedItem.objects.all()
    return render(request, 'saved_items.html', {'items': items})


def saved_items_view(request):
    if request.method == 'POST':
        form = SavedItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('saved_items')  # Redireciona para a mesma página após salvar o item
    else:
        form = SavedItemForm()

    items = SavedItem.objects.all()
    return render(request, 'saved_items.html', {'items': items, 'form': form})

def item_cadastrado(request):
    items = SavedItem.objects.all()
    return render(request, 'item_cadastrado.html', {'items': items})


# View para editar um item
def edit_item_view(request, item_id):
    item = get_object_or_404(SavedItem, id=item_id)
    if request.method == 'POST':
        form = SavedItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('saved_items')
    else:
        form = SavedItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})

# View para excluir um item
def delete_item_view(request, item_id):
    item = get_object_or_404(SavedItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('saved_items')

    return render(request, 'delete_item.html', {'item': item})

#Fim teste Views

@login_required 
def dashboard(request):
     request.session['user_name'] = request.user.username
     return render(request, 'dashboard.html',)

def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validação de senhas
        if not senha == confirmar_senha:
            print(1)
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('cadastrar')
        
        if len(senha) < 6:
            print(2)
            messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 caracteres')
            return redirect('cadastrar')
        
        users = User.objects.filter(username=username)

        if users.exists():
            print(3)
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username')
            return redirect('cadastrar')
        
        users_email = User.objects.filter(email=email)
        if users_email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse email')
            return redirect('cadastrar')
        
        user = User.objects.create_user(
            username=username,
            password=senha,
            email=email,
            first_name=nome,
            last_name=sobrenome
        )

        return redirect('login') 

def login(request):
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')

def feminino(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'feminino.html', {'user_name': user_name})

def masculino(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'masculino.html', {'user_name': user_name})

def acessorios(request):
    #user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'acessorios.html',) #{'user_name': user_name})

def central_atendimento(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'central_atendimento.html', {'user_name': user_name})

# Marcas
def fila(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'fila.html', {'user_name': user_name})

def olympikus(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'olympikus.html', {'user_name': user_name})

def adidas(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'adidas.html', {'user_name': user_name})

def puma(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'puma.html', {'user_name': user_name})

def reebok(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'reebok.html', {'user_name': user_name})

def nike(request):
    user_name = request.session.get('user_name', 'Visitante')
    return render(request, 'nike.html', {'user_name': user_name})

@permission_required('core.permissao_01') 
def recuperar_senha(request):
    return render(request, 'recuperar_senha.html')


#Crud teste
@permission_required('core.permissao_01')
def listar_usuarios_test(request):
    usuarios = Usuario.objects.all()
    context = {
        'dados_usuario':usuarios
    }
    return render(request,'perfil.html',context)

@permission_required('core.permissao_01')
def cadastro_test(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios_test')
    context = {
        'form_usuario':form
    }
    return render(request,'cadastro_test.html',context)

@permission_required('core.permissao_01')
def editar_usuario(request,id):
    usuario = Usuario.objects.get(pk=id)

    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios_test')
    
    context = {
        'form_usuario':form
    }
    return render(request,'cadastro_test.html',context)

@permission_required('core.permissao_01')
def remover_usuario(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios_test')

#! === Produto ===
# Create (Criar)
@permission_required('core.permissao_01')
def produto_criar(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('produto_listar')
    context = {
        'form_produto': form
    }
    return render(request, 'produto_criar.html', context)

# Read (Ler)
@permission_required('core.permissao_01')
def produto_listar(request):
    produtos = Produto.objects.all()
    context = {
        'dados_produto': produtos
    }
    return render(request, 'produto_listar.html', context)

# Update (Atualizar)
@permission_required('core.permissao_01')
def produto_atualizar(request, id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produto_listar')
    context = {
        'form_produto': form
    }
    return render(request, 'produto_criar.html', context)

# Delete (Deletar)
@permission_required('core.permissao_01')
def produto_deletar(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect('produto_listar')

#! === Fornecedor ===
@permission_required('core.permissao_01')
# Create (Criar)
def fornecedor_criar(request):
    form = FornecedorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_listar')
    context = {
        'form_fornecedor': form
    }
    return render(request, 'fornecedor_criar.html', context)

@permission_required('core.permissao_01')
# Read (Ler)
def fornecedor_listar(request):
    fornecedors = Fornecedor.objects.all()
    context = {
        'dados_fornecedor': fornecedors
    }
    return render(request, 'fornecedor_listar.html', context)

@permission_required('core.permissao_01')
# Update (Atualizar)
def fornecedor_atualizar(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    form = FornecedorForm(request.POST or None, request.FILES or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_listar')
    context = {
        'form_fornecedor': form
    }
    return render(request, 'fornecedor_criar.html', context)

@permission_required('core.permissao_01')
# Delete (Deletar)
def fornecedor_deletar(request, id):
    fornecedor = Fornecedor.objects.get(pk=id)
    fornecedor.delete()
    return redirect('fornecedor_listar')

