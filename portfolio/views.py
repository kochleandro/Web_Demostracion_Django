from django.shortcuts import render
from .models import Proyecto
# Create your views here.

def portfolio(request):
    """
    Render al HTML de portfolio
    """
    proyectos = Proyecto.objects.all()
    imagen_de_fondo_ccs = 'portfolio'
    active_nav = 'portfolio'
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav,
        'proyectos' : proyectos,
    }
    return render(request, 'portfolio/portfolio.html', contexto)