from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import *

# Agregar la clase Estudiante para administrar desde
# interfaz de administración
admin.site.register(Persona)
admin.site.register(Barrio)
admin.site.register(Casas)
admin.site.register(Departamentos)
# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
