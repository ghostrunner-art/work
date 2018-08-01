from django.contrib import admin
from .models import Daan,Wenti

@admin.register(Daan)
class Daan(admin.ModelAdmin):
    pass
