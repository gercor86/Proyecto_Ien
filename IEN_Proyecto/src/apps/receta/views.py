from django.shortcuts import render
from .forms import  RecetaForm1
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from .models import Dulce
from django.urls import  reverse_lazy

class Base(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'base.html')

class Dulce_v(View):
    def get(self, request, *args, **kwargs):

        lista_dulce = Dulce.objects.all()

        context = {
            
            'dulce_lista' : lista_dulce
        }

         
        return render(request, 'dulce.html', context)


class Detalle_dulce_v(View):
    def get(self, request, *args, **kwargs):

        return render(request,'bizcochuelo.html')

class pionono(View):
    def get(self, request, *args, **kwargs):

        return render(request,'pionono.html')

class pan_campo(View):
    def get(self,request, *args, **kwargs):

        return render(request, 'pan_campo.html')



def crear_receta(request):

    template = 'crear_recetas.html'

    context = {}

    if request.method == 'GET':
        form = RecetaForm1()

    if request.method == 'POST':

        Dulce.objects.create(nombre= request.POST['nombre', 'tipo'])
        return render(request, 'receta/base.html')

    return render(request, template, context)


class Receta3(CreateView):
    model = Dulce
    template_name = 'crear_recetas.html'
    form_class = RecetaForm1
    success_url = reverse_lazy('receta_dulce')


class actualizar_receta(UpdateView):
    model = Dulce
    template_name = 'actualizar_receta.html'
    fields = ['nombre', 'tipo']
    success_url = reverse_lazy('receta_dulce')

class eliminar_receta(DeleteView):
    model = Dulce
    template_name = 'eliminar_receta.html'
    fields = ['nombre', 'tipo']
    success_url = reverse_lazy('receta_dulce')

class vista_receta(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'vista_receta.html')

class figacita_manteca(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'figacita_de_manteca.html')

class pan_viena(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'pan_viena.html')

class bizcochito_grasa(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'bizcochitos_grasa.html')

class pan_salvado(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'pan_salvado.html')

class panes_saborizados(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'panes_saborizados.html')

class galletas_marineras(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'galletas_marineras.html')

class berlinesas_donas(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'berlinesas_donas.html')

class grisines_tradiconales(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'grisines_tradicionales.html')

class pan_de_leche_miguelitos(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'pan_de_leche_miguelitos.html')

class medialunas_saladas_manteca(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'medialunas_saladas_manteca.html')

class facaccia_rellena(View):
    def get(self, request, *args, **kwargs):

        return render(request,'facaccia_rellena.html')

class pizza(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'pizza.html')

class brioche(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'brioche.html')

class empanada_carne(View):
    def get(set, request, *args, **kwargs):

        return render(request, 'empanada_carne.html')

class empanada_criolla(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'empanada_criolla.html')