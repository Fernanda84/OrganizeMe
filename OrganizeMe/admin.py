from django.contrib import admin

from .models import Atividade, Perfil, UserCostumizado


admin.site.register(UserCostumizado)
admin.site.register(Atividade)
admin.site.register(Perfil)

