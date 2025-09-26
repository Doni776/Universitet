from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Yonalish, Fan, Ustoz
from django.contrib.auth.models import Group,   User



class FanInline(TabularInline):
    model = Fan
    extra = 1
    fields = ("nom", "asosiy", "yonalish")



class UstozInline(TabularInline):
    model = Ustoz
    extra = 1
    fields = ("ism", "yosh", "jins", "daraja")


@admin.register(Yonalish)
class YonalishAdmin(ModelAdmin):
    list_display = ("nom", "aktiv")
    list_filter = ("aktiv",)
    search_fields = ("nom",)
    inlines = [FanInline]


@admin.register(Fan)
class FanAdmin(ModelAdmin):
    list_display = ("nom", "asosiy", "yonalish")
    list_filter = ("asosiy", "yonalish")
    search_fields = ("nom",)
    inlines = [UstozInline]


@admin.register(Ustoz)
class UstozAdmin(ModelAdmin):
    list_display = ("ism", "yosh", "jins", "daraja", "fan")
    list_filter = ("jins", "daraja", "fan")
    search_fields = ("ism",)

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "Universitet Admin paneli"
admin.site.site_title = "Universitet boshqaruvi"
admin.site.index_title = "Admin paneli"