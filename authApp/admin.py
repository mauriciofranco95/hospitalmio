from django.contrib import admin
from .models.usuario import Usuario
from .models.psalud import Personal_salud
from .models.paciente import Paciente
from .models.familiar import Familiar

admin.site.register(Usuario)
admin.site.register(Personal_salud)
admin.site.register(Paciente)
admin.site.register(Familiar)

# Register your models here.
