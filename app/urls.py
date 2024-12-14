from django.urls import path
from .views import DeleteViewTelefone, FormViewUsuario, FormViewTelefone, UpdateViewUsuario, DeleteViewUsuario, ListViewUsuario, ListViewTelefone

urlpatterns = [
    path('formulario_usuario/', FormViewUsuario.as_view(),name="formulario_usuario"),
    path('usuarios/editar_usuario/<int:pk>', UpdateViewUsuario.as_view(), name="editar_usuarios"),
    path('usuarios/deletar_usuario/<int:pk>', DeleteViewUsuario.as_view(), name="deletar_usuario"),
    path('usuarios/formulario_telefone/<int:pk>', FormViewTelefone.as_view(), name="formulario_telefone"),
    path('usuarios/', ListViewUsuario.as_view(), name="lista_usuarios"),
    path('usuarios/telefones/<int:pk>/', ListViewTelefone.as_view(), name="lista_telefones"),
    path('usuarios/telefones/deletar_telefone/<int:pk>/', DeleteViewTelefone.as_view(), name="deletar_telefone")
]