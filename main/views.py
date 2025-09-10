from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def fan_delete(request, pk):
    fan = get_object_or_404(Fan, pk=pk)
    if request.method == "POST":
        fan.delete()
        return redirect("fan_list")
    return render(request, "fan_confirm_delete.html", {"fan": fan})


def yonalish_delete(request, pk):
    yonalish = get_object_or_404(Yonalish, pk=pk)
    if request.method == "POST":
        yonalish.delete()
        return redirect("yonalish_list")
    return render(request, "yonalish_confirm_delete.html", {"yonalish": yonalish})


def fan_list(request):
    q = request.GET.get("q")
    if q:
        fanlar = Fan.objects.filter(nom__icontains=q)
    else:
        fanlar = Fan.objects.all()
    return render(request, "fan_list.html", {"fanlar": fanlar})


def ustoz_list(request):
    q = request.GET.get("q")
    if q:
        ustozlar = Ustoz.objects.filter(ism__icontains=q)
    else:
        ustozlar = Ustoz.objects.all()
    return render(request, "ustoz_list.html", {"ustozlar": ustozlar})


def ustoz_delete(request, pk):
    ustoz = get_object_or_404(Ustoz, pk=pk)
    if request.method == "POST":
        ustoz.delete()
        return redirect("ustoz_list")
    return render(request, "ustoz_confirm_delete.html", {"ustoz": ustoz})


def yonalish_list(request):
    yonalishlar = Yonalish.objects.all()
    return render(request, "yonalish_list.html", {"yonalishlar": yonalishlar})

def home(request):
    return render(request, "home.html")

