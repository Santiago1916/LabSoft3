from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse



# Create your views here.

from .models import Usuario, CategoriaCoctel, Coctel, Imagen, Licor

def inicio(request):
    '''
    La ruta por defecto que enumera todos los cocteles
    '''
    return verListaCocteles(request)

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        confirmacion = request.POST['confirmacion']
        if contrasena != confirmacion:
            return render(request, 'registro.html', {
                'mensaje': 'Las contraseñas deben coincidir.',
                'categoria': CategoriaCoctel.objects.all()
            })
        try:
            usuario = Usuario.objects.create_user(usuario, email, contrasena)
            usuario.save()
        except IntegrityError:
            return render(request, 'registro.html', {
                'mensaje': 'Nombre de usuario ya ocupado',
                'categoria': CategoriaCoctel.objects.all()
            })
        login(request, usuario)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'registro.html', {
            'categorias': CategoriaCoctel.objects.all()
        })


def vistaInicioSesion(request):
    if request.method == 'POST':

        nombreUsuario = request.POST['usuario']
        contrasena = request.POST['contrasena']
        usuario = authenticate(request, username=nombreUsuario, password=contrasena)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect(reverse('inicio'))
        else:
            return render(request, 'registro.html', {
                'mensaje': 'Es incorrecto el usuario o la contrasena',
                'categorias': CategoriaCoctel.objects.all()
            })
    else:
        return render(request, 'registro.html',  {
            'categorias': CategoriaCoctel.objects.all()
        })


def vistaCierreInicioSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('inicio'))


def verListaCocteles(request):
    Coctel = Coctel.objects.all()

    for Coctel in Coctel:
        Coctel.image = Coctel.get_images.first()

    pagina = request.GET.get('pagina', 1)
    paginador = Paginator(Coctel, 4)
    try:
        pagina = paginador.page(pagina)
    except PageNotAnInteger:
        pagina = paginador.page(1)
    except EmptyPage:
        pagina = paginador.page(paginador.num_pages)

    return render(request, 'inicio.html', {
        'categorias': CategoriaCoctel.objects.all(),
        'cocteles': Coctel,
        'paginas': pagina,
        'titulo': 'Lista de cocteles'
    })

def vistaDetallesCocteles(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    coctel = Coctel.objects.get(id=id)

    return render(request, 'food.html', {
        'categories': CategoriaCoctel.objects.all(),
        'food': coctel,
        'images': coctel.get_images.all(),
    })

@login_required
def food_add_view(request):
    '''
    It allows the user to add a new food item
    '''
    ImageFormSet = forms.modelformset_factory(Image, form=ImageForm, extra=2)

    if request.method == 'POST':
        food_form = FoodForm(request.POST, request.FILES)
        image_form = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

        if food_form.is_valid() and image_form.is_valid():
            new_food = food_form.save(commit=False)
            new_food.save()

            for food_form in image_form.cleaned_data:
                if food_form:
                    image = food_form['image']

                    new_image = Image(food=new_food, image=image)
                    new_image.save()

            return render(request, 'food_add.html', {
                'categories': FoodCategory.objects.all(),
                'food_form': FoodForm(),
                'image_form': ImageFormSet(queryset=Image.objects.none()),
                'success': True
            })
        
        else:
            return render(request, 'food_add.html', {
                'categories': FoodCategory.objects.all(),
                'food_form': FoodForm(),
                'image_form': ImageFormSet(queryset=Image.objects.none()),
            })

    else:
        return render(request, 'food_add.html', {
            'categories': FoodCategory.objects.all(),
            'food_form': FoodForm(),
            'image_form': ImageFormSet(queryset=Image.objects.none()),
        })
    

@login_required
def food_log_view(request):
    '''
    It allows the user to select food items and 
    add them to their food log
    '''
    if request.method == 'POST':
        foods = Food.objects.all()

        # get the food item selected by the user
        food = request.POST['food_consumed']
        food_consumed = Food.objects.get(food_name=food)

        # get the currently logged in user
        user = request.user
        
        # add selected food to the food log
        food_log = FoodLog(user=user, food_consumed=food_consumed)
        food_log.save()

    else: # GET method
        foods = Food.objects.all()
        
    # get the food log of the logged in user
    user_food_log = FoodLog.objects.filter(user=request.user)
    
    return render(request, 'food_log.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'user_food_log': user_food_log
    })


@login_required
def food_log_delete(request, food_id):
    '''
    It allows the user to delete food items from their food log
    '''
    # get the food log of the logged in user
    food_consumed = FoodLog.objects.filter(id=food_id)

    if request.method == 'POST':
        food_consumed.delete()
        return redirect('food_log')
    
    return render(request, 'food_log_delete.html', {
        'categories': FoodCategory.objects.all()
    })


def categories_view(request):
    '''
    It renders a list of all food categories
    '''
    return render(request, 'categories.html', {
        'categories': FoodCategory.objects.all()
    })


def category_details_view(request, category_name):
    '''
    Clicking on the name of any category takes the user to a page that 
    displays all of the foods in that category
    Food items are paginated: 4 per page
    '''
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    category = FoodCategory.objects.get(category_name=category_name)
    foods = Food.objects.filter(category=category)

    for food in foods:
        food.image = food.get_images.first()

    # Show 4 food items per page
    page = request.GET.get('page', 1)
    paginator = Paginator(foods, 4)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'food_category.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'foods_count': foods.count(),
        'pages': pages,
        'title': category.category_name
    })
