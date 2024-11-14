from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Fotos(models.Model):
    fechaHora = models.DateTimeField(default=timezone.now)
    emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    texto = models.TextField(null=True,blank=True)