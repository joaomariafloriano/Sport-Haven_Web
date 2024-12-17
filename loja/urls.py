from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
#Testanto Path
    path('saved-items/', views.saved_items_view, name='saved_items'),
    path('saved-items/edit/<int:item_id>/', views.edit_item_view, name='edit_item'),
    path('saved-items/delete/<int:item_id>/', views.delete_item_view, name='delete_item'),
    path('item_cadastrado/', views.item_cadastrado, name='item_cadastrado'),
#Fim teste Path
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('recuperar_senha/', views.recuperar_senha, name="recuperar_senha"),

    path('feminino/', views.feminino, name="feminino"),
    path('masculino/', views.masculino, name="masculino"),
    path('acessorios/', views.acessorios, name="acessorios"),
    path('central_atendimento/', views.central_atendimento, name="central_atendimento"),
    
    path('fila/', views.fila, name="fila"),
    path('nike/', views.nike, name="nike"),
    path('puma/', views.puma, name="puma"),
    path('reebok/', views.reebok, name="reebok"),
    path('adidas/', views.adidas, name="adidas"),
    path('olympikus/', views.olympikus, name="olympikus"),

    # Funcionários
    path('perfil/', views.listar_usuarios_test, name="listar_usuarios_test"),
    path('cadastro_test/', views.cadastro_test, name="cadastro_test"),
    path('editar_usuario/<int:id>', views.editar_usuario, name="editar_usuario"),
    path('remover_usuario/<int:id>', views.remover_usuario, name="remover_usuario"),

    # Produto
    path('produto_criar/', views.produto_criar, name="produto_criar"),
    path('produto_listar/', views.produto_listar, name="produto_listar"),
    path('produto_atualizar/<int:id>', views.produto_atualizar, name="produto_atualizar"),
    path('produto_deletar/<int:id>', views.produto_deletar, name="produto_deletar"),

    # Fornecedor
    path('fornecedor_criar/', views.fornecedor_criar, name="fornecedor_criar"),
    path('fornecedor_listar/', views.fornecedor_listar, name="fornecedor_listar"),
    path('fornecedor_atualizar/<int:id>', views.fornecedor_atualizar, name="fornecedor_atualizar"),
    path('fornecedor_deletar/<int:id>', views.fornecedor_deletar, name="fornecedor_deletar"),

    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    #path('cadastro/', views.cadastro, name="cadastro"),

    path('cadastrar/', views.cadastrar, name="cadastrar"),

    path('perfil/', views.listar_usuarios_test, name="listar_usuarios_test"),
    path('cadastro_test/', views.cadastro_test, name="cadastro_test"),
    path('editar_usuario/<int:id>', views.editar_usuario, name="editar_usuario"),
    path('remover_usuario/<int:id>', views.remover_usuario, name="remover_usuario"),

    path('recuperar_senha/', views.recuperar_senha, name="recuperar_senha"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)