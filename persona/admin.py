from django.contrib import admin

# Register your models here.
from .models import Personal
from .models import Cliente
from .models import Proveedor


admin.site.register(Personal)
admin.site.register(Cliente)
admin.site.register(Proveedor)