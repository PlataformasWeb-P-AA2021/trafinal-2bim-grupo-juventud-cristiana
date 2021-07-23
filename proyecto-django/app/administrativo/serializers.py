from django.contrib.auth.models import User, Group
from administrativo.models import *

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrio
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__' 


class CasasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Casas
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__' 
        
class DepartamentosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamentos
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__' 