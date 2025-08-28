from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=200)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Fan(models.Model):
    nom = models.CharField(max_length=200)
    asosiy = models.BooleanField(default=False)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    JINS_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    ]
    DARAJA_CHOICES = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
    ]

    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    jins = models.CharField(max_length=10, choices=JINS_CHOICES)
    daraja = models.CharField(max_length=10, choices=DARAJA_CHOICES)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

