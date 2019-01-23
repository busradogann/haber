from django.db import models
from django.utils import timezone

class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yayinlanma_tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
