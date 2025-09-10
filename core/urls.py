
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("yonalishlar/", yonalish_list, name="yonalish_list"),
    path("yonalish/<int:pk>/delete/", yonalish_delete, name="yonalish_delete"),
    path("fanlar/", fan_list, name="fan_list"),
    path("fan/<int:pk>/delete/", fan_delete, name="fan_delete"),
    path("ustozlar/", ustoz_list, name="ustoz_list"),
    path("ustoz/<int:pk>/delete/", ustoz_delete, name="ustoz_delete"),
]
