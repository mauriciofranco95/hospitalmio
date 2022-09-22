from django.db import models
from .usuario import Usuario
from .psalud import Personal_salud

class Paciente(models.Model):
    id_paciente=models.AutoField(primary_key=True)
    id_Psalud=models.ForeignKey(Personal_salud, related_name='paciente', on_delete=models.CASCADE)
    username=models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    ciudad=models.CharField('Ciudad', max_length=45)
    fechadenacimiento=models.DateField('Fecha de nacimiento')
    dirección=models.CharField('direccion', max_length=45)