from django.shortcuts import render, redirect
import requests
from datetime import datetime
import pytz

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm


# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def inicia_crea_sesion(request):
    return render(request, 'core/inicia_crea_sesion.html')

def lo_mas_vendido(request):
    return render(request, "core/lo_mas_vendido.html")

def index_view(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, "core/carrito.html")

def new(request):
    return render(request, "core/new.html")

def halo_infinite_producto(request):
    return render(request, "core/halo_infinite_producto.html")

def halo_ce_producto(request):
    return render(request, "core/halo_ce_producto.html")

def destiny_producto(request):
    return render(request, "core/destiny_producto.html")

def FF7_producto(request):
    return render(request, "core/FF7_producto.html")

def codmw2_producto(request):
    return render(request, "core/codmw2_producto.html")

def spiderman_producto(request):
    return render(request, "core/spiderman_producto.html")

def bf_2042_producto(request):
    return render(request, "core/bf_2042_producto.html")

def elden_ring_producto(request):
    return render(request, "core/elden_ring_producto.html")

def modificar_usuario(request):
    return render(request, "core/modificar_usuario.html")


def obtener_tipo_cambio():
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": "PTDPbjtjEFQljw0w20FCeGbHnKNY5e0k"}
    parametros = {"from": "USD", "to": "CLP", "amount": 1}
    
    response = requests.get(url, headers=headers, params=parametros)
    
    if response.status_code == 200:
        tipo_cambio = response.json()["result"]
    else:
        tipo_cambio = "Error al obtener el tipo de cambio"
    
    return tipo_cambio

def index(request):
    tipo_cambio = obtener_tipo_cambio()
    return render(request, "core/index.html", {"tipo_cambio": tipo_cambio})

def obtener_clima(ciudad):
    api_key = "3dc41b1f91027914804e7e5439a814ba"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperatura = data["main"]["temp"]
        tiempo_unix = data["dt"]
        zona_horaria = data["timezone"]
        print(f"Temperatura: {temperatura}, Tiempo UNIX: {tiempo_unix}, Zona horaria: {zona_horaria}")  # Mensaje de depuración
        return temperatura, tiempo_unix, zona_horaria
    else:
        print(f"Error al obtener datos de la API de OpenWeatherMap. Código de estado: {response.status_code}")  # Mensaje de depuración
        return None, None, None

def convertir_unix_a_hora(tiempo_unix, zona_horaria):
    if tiempo_unix is not None and zona_horaria is not None:
        hora_local = datetime.utcfromtimestamp(tiempo_unix + zona_horaria)
        return hora_local.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None

def index(request):
    ciudad = "Santiago,cl"  # Reemplaza con la ciudad deseada
    temperatura, tiempo_unix, zona_horaria = obtener_clima(ciudad)
    hora_local = convertir_unix_a_hora(tiempo_unix, zona_horaria)
    tipo_cambio = obtener_tipo_cambio()
    
    context = {
        "temperatura": temperatura,
        "hora_local": hora_local,
        "tipo_cambio": tipo_cambio
    }
    
    return render(request, "core/index.html", context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('core:index')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def index(request):
    return render(request, 'core/index.html')






