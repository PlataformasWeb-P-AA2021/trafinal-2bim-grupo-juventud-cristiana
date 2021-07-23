from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import *

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    casas = 'Casas.objects.all()'
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'casas': casas}
    return render(request, 'index.html', informacion_template)

def listar_casas(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    casas = Casas.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'casas': casas}
    return render(request, 'listar_casas.html', informacion_template)

def listar_departamentos(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    departamentos = Departamentos.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'departamentos': departamentos}
    return render(request, 'listar_departamentos.html', informacion_template)


def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

def obtener_persona(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    persona = Persona.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'persona': persona}
    return render(request, 'obtener_persona.html', informacion_template)


@login_required(login_url='/entrando/login/')
# @permission_required('administrativo.add_estudiante', )
@permission_required('administrativo.add_persona', login_url="/entrando/login/")
def crear_persona(request):
    """
    """
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)


@login_required(login_url='/entrando/login/')
def editar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)


def eliminar_persona(request, id):
    """
    """
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)


def crear_barrio(request):
    """
    """

    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)


def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)



def eliminar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.add_casa', login_url="/entrando/login/")
def editar_casa(request, id):
    """
    """
    casa = Casas.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasasForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasasForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.add_casa', login_url="/entrando/login/")
def eliminar_casa(request, id):
    """
    """
    persona = Casas.objects.get(pk=id)
    persona.delete()
    return redirect(index)


@login_required(login_url='/entrando/login/')
@permission_required('administrativo.add_casa', login_url="/entrando/login/")
def editar_departamento(request, id):
    """
    """
    casa = Departamentos.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentosForm(request.POST, instance=casa)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasasForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('administrativo.add_casa', login_url="/entrando/login/")
def eliminar_departamento(request, id):
    """
    """
    persona = Departamentos.objects.get(pk=id)
    persona.delete()
    return redirect(index)











# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioViewSet(viewsets.ModelViewSet):
#class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CasasViewSet(viewsets.ModelViewSet):
#class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Casas.objects.all()
    serializer_class = CasasSerializer
    # permission_classes = [permissions.IsAuthenticated]

class DepartamentosViewSet(viewsets.ModelViewSet):
#class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
    # permission_classes = [permissions.IsAuthenticated]