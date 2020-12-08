from django.contrib import admin
from .models import Rescatado

# Register your models here.
class RescatadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Rescatado, RescatadoAdmin)