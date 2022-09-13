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

class figacita_manteca(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'figacita_de_manteca.html')

class pan_viena(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'pan_viena.html')