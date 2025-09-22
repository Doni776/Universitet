from django.contrib import admin
from .models import Yonalish,Fan,Ustoz
from django.contrib.auth.models import Group, User

class UstozAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "yosh", "jins", "daraja", "fan")
    search_fields = ("ism",)

class YonalishAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "aktiv")
    list_filter = ("aktiv",)
    search_fields = ("nom",)

class FanAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "asosiy", "yonalish")
    list_filter = ("asosiy", "yonalish")
    search_fields = ("nom",)


admin.site.register(Yonalish,YonalishAdmin)
admin.site.register(Fan,FanAdmin)
admin.site.register(Ustoz,UstozAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Universitet Admin paneli"
admin.site.site_title = "Universitet boshqaruvi"
admin.site.index_title = "Admin paneli"