from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.cedula,
                self.correo)

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s  %s" % (self.nombre,
                self.siglas)
#casas son: propietario (de tipo Persona), dirección, barrio 
#(de tipo Barrio), valor de bien, color de inmueble, número de cuartos, número de pisos.

class Casas(models.Model):
    barrio =  models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrios")
    direccion = models.CharField(max_length=100)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="propietarios")
    valor = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    cuartos = models.CharField(max_length=30)
    pisos = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s %s" % (self.valor, self.cuartos)

#departamentos son: propietario (de tipo Persona), dirección, 
#barrio (de tipo Barrio), valor del bien, número de cuartos, valor mensual de mantenimiento.
class Departamentos(models.Model):
    barrio =  models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barriosd")
    direccion = models.CharField(max_length=100)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="propietariosd")
    valor = models.CharField(max_length=30)
    cuartos = models.CharField(max_length=30)
    mensual = models.CharField(max_length=30)
    
    def __str__(self):
        return "%s %s" % (self.valor, self.cuartos)

