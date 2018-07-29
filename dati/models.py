from django.db import models

class Daan(models.Model):
    daan = models.CharField(max_length=15)
    panduan = models.BooleanField(default= False)

class Wenti(models.Model):
    wenti_on = models.ForeignKey(Daan,on_delete=models.CASCADE)
