from django.db import models

# Create your models here.
class temas (models.Model):    #este es el nombre de la tabla
    nombre = models.CharField(max_length=100, unique=True) #esta es una columna de la tabla, es de tipo string alfanumerico con longitud maxima de 100 y de nombre unico que no se puede repetir

class webs (models.Model):
    tema = models.ForeignKey(temas, on_delete=models.CASCADE)#esto dice que la llave foranea de esta tabla "webs" sera un "tema". el "tema" provendra de la tabla de ariba y ahi ya hemos creado una relacion entre 2 tablas 
    nombre = models.CharField(max_length=100, unique=True) #esta es una columna de la tabla, es de tipo string alfanumerico con longitud maxima de 100 y de nombre unico que no se puede repetir
    ruta = models.URLField(unique=True) #esta es una columna de la tabla, es de tipo url con longitud maxima de 100 y de nombre unico que no se puede repetir