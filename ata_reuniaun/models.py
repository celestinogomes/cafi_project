from django.db import models
import os
# Create your models here.

class Ata(models.Model):
    no_ata = models.CharField(max_length=50, unique=True)
    linha_ministerio = models.CharField(max_length=50)
    asunto = models.TextField(max_length=1000)
    data_ata = models.DateField()
    diversos = models.CharField(max_length=200)
    file_attachment = models.FileField(upload_to='ata/')

    def __str__(self):
        return self.asunto

    class Meta:
        verbose_name = 'ATA Reuniaun'
        verbose_name_plural = 'ATA Reuniaun'
    
    def delete(self, *args, **kwargs):
        if self.file_attachment:
            os.remove(self.file_attachment.path)
        super().delete(*args, **kwargs)