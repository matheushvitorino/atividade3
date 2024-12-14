from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from app.forms import FormularioUsuario,FormularioTelefone
from app.models import Usuario,Telefone
from django.views.generic.edit import FormView,UpdateView,DeleteView
from django.views.generic.list import ListView


class FormViewUsuario(FormView):
    template_name = "TemplateUsuario.html"
    form_class = FormularioUsuario
    success_url = reverse_lazy('lista_usuarios')

    def form_valid(self,form):
        nome = form.cleaned_data['nome']
        Usuario.objects.create(nome=nome)
        return super().form_valid(form)
        
class UpdateViewUsuario(UpdateView):
    model= Usuario
    template_name="TemplateEditarUsuario.html"
    fields=['nome']
    success_url = reverse_lazy('lista_usuarios')
    
class DeleteViewUsuario(DeleteView):
    model = Usuario
    template_name="TemplateDeletarUsuario.html"
    success_url = reverse_lazy('lista_usuarios')
    
class ListViewUsuario(ListView):
    model= Usuario
    template_name="TemplateListaUsuario.html"
    context_object_name="usuarios"
    
class FormViewTelefone(FormView):
    
    template_name = "TemplateTelefone.html"
    form_class = FormularioTelefone
    success_url = reverse_lazy('lista_usuarios')
    
    def form_valid(self,form):
        numero = form.cleaned_data['numero']
        usuario_id = get_object_or_404(Usuario, pk=self.kwargs['pk'])
        Telefone.objects.create(numero=numero, usuario_id=usuario_id)
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        pk = get_object_or_404(Usuario, pk=id)
        context['usuario'] = pk
        return context
    
class ListViewTelefone(ListView):
    model= Telefone
    template_name="TemplateListaTelefone.html"
    context_object_name="telefones"

    def get_queryset(self):
        usuario_id = self.kwargs['pk']
        return Telefone.objects.filter(usuario_id=usuario_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        pk = get_object_or_404(Usuario, pk=id)
        context['usuario'] = pk
        return context
    
class DeleteViewTelefone(DeleteView):
    model = Telefone
    template_name="TemplateDeletarTelefone.html"
    def get_success_url(self):
        usuario_id = self.object.usuario_id.pk        
        return reverse_lazy('lista_telefones', kwargs={'pk': usuario_id})