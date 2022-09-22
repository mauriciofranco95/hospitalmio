from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    id_familiar=models.AutoField(primary_key=True)
    username=models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    id_paciente=models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    parentesco=models.CharField('Parentesco', max_length=45)
    correo=models.CharField('Correo', max_length=45)