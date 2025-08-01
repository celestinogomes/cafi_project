from django.db import models
import os

class Deliberasaun(models.Model):
    no_cafi = models.CharField(max_length=50, primary_key=True)
    linha_ministerio = models.CharField(max_length=50)
    asunto = models.TextField(max_length=1000)
    data_cafi = models.DateField()
    observasaun = models.TextField()
    file_attachment = models.FileField(upload_to='deliberasaun/')
    anexo = models.FileField(upload_to='anexo')

    def __str__(self):
        return self.asunto

    class Meta:
        verbose_name = 'deliberasaun'
        verbose_name_plural = 'deliberasaun'
    
    def delete(self, *args, **kwargs):
        if self.file_attachment:
            os.remove(self.file_attachment.path)
        super().delete(*args, **kwargs)