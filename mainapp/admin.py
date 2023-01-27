from django.contrib import admin
from .models import Personas

# Register your models here.

class PersonasAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'create_at', 'update_at')
    search_fields = ('cedula', 'user__username', 'fNacimiento')
    list_filter = ('public',)
    list_display = ('cedula', 'public', 'create_at', 'user')
    ordering = ('-create_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Personas, PersonasAdmin)
