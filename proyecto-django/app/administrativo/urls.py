"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('casas', views.listar_casas, name='listar_casas'),
        path('departamentos', views.listar_departamentos, name='listar_departamentos'),
        path('persona/<int:id>', views.obtener_persona,
            name='obtener_persona'),
        path('crear/persona', views.crear_persona,
            name='crear_persona'),
        path('editar_persona/<int:id>', views.editar_persona,
            name='editar_persona'),
        path('eliminar/persona/<int:id>', views.eliminar_persona,
            name='eliminar_persona'),
        # numeros telefonicos
        path('crear/barrio', views.crear_barrio,
            name='crear_barrio'),
        path('editar/barrio/<int:id>', views.editar_barrio,
            name='editar_barrio'),
        path('eliminar/barrio/<int:id>', views.eliminar_barrio,
            name='eliminar_barrio'),
        # departamentos
        #path('crear/departamento', views.crear_departamento,
        #    name='crear_departamento'),
        path('editar/departamento/<int:id>', views.editar_departamento,
            name='editar_departamento'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento,
            name='eliminar_departamento'),
        #path('departamento/<int:id>', views.obtener_departamento,
        #    name='obtener_departamento'),
        # casas
        
        path('editar/casa/<int:id>', views.editar_casa,
            name='editar_casa'),
        path('eliminar/casa/<int:id>', views.eliminar_casa,
            name='eliminar_casa'),
        #path('casa/<int:id>', views.eliminar_casa,
        #    name='obtener_casa'),
        
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
