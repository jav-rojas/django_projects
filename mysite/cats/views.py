from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
#from autos.forms import MakeForm

# Creación de views

'''
View principal, es decir, asociada a /autos/. Es una clase que hereda LoginRequiredMixin
para acceder a la funcionalidad de requerir login para poder ser vista. Hereda también la
clase View.
'''
class MainView(LoginRequiredMixin, View):
    # Lo que hace si recibe una solicitud get.
    def get(self, request):
        # Cuenta todos los objetos del modelo Make
        mc = Breed.objects.all().count()
        # Muestra todos los objetos del modelo Auto
        al = Cat.objects.all()

        # Agrega como ctx el número ('make_count') y la lista ('auto_list')
        ctx = {'breed_count': mc, 'cat_list': al}
        # Devuelve como resultado auto_list.html en nombre-app/autos/templates/autos utilizando el contexto ctx
        return render(request, 'cats/cat_list.html', ctx)

'''
View que muestra a los fabricantes actuales.
'''
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        # Obtiene del modelo Make todos los objetos
        ml = Breed.objects.all()
        # Lo agrega como ctx
        ctx = {'breed_list': ml}
        # Utiliza ctx y template para enviar la respuesta
        return render(request, 'cats/breed_list.html', ctx)

'''
Views para el CRUD de fabricante y modelo de automóvil, utilizando Generic Views
Ver bajo estas views para encontrar el código para hacerlo manualmente.

Los templates por defecto son:

    - Para Create, busca _form. Ejemplo, si el modelo es "Make", buscará make_form.html
    - Para Update, busca _form. Ejemplo, si el modelo es "Make", buscará make_form.html
    - Para Delete, busca _confirm_delete. Ejemplo, si el modelo es "Make", buscará make_confirm_delete

Para cambiar el template por defecto, estas generic views tienen un attribute "template_name_suffix"
que puede ser modificado para cambiar el nombre del template por defecto.
'''

class BreedCreate(LoginRequiredMixin, CreateView):
    # Selecciona el modelo a utilizar
    model = Breed
    # Los campos de ese modelo que deseamos mostrar en el formulario
    fields = '__all__'
    # La URL en caso de respuesta satisfactoria
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

'''
Este es un ejemplo de una clase create, por ejemplo, creada manualmente

class MakeCreate(LoginRequiredMixin, View):
    # El template a usar
    template = 'autos/make_form.html'
    # URL a la que va si la respuesta es satisfactoria
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        # MakeForm es una clase en forms.py
        form = MakeForm()
        # Pasa como ctx el formulario
        ctx = {'form': form}
        # Devuelve la respuesta habiendo usado ese formulario en el template
        return render(request, self.template, ctx)

    def post(self, request):
        # Misma clase de forms.py, pero en POST
        form = MakeForm(request.POST)
        # Realiza validaciones. Si falla, vuelve al cuestionario
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        # Si no falla, guarda el formulario y sus datos
        make = form.save()
        # Y retorna la URL de respuesta satisfactoria
        return redirect(self.success_url)
'''

'''
Esta es una clase generica para crear a partir de un modelo

class AutoCreate(LoginRequiredMixin, CreateView):
    # Selecciona el modelo a utilizar
    model = Auto
    # Los campos de ese modelo que deseamos mostrar en el formulario
    fields = '__all__'
    # La URL en caso de respuesta satisfactoria
    success_url = reverse_lazy('autos:all')
'''

