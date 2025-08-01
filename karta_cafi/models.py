from django.db import models
import os

class ConviteCafi(models.Model):
    no_referensia = models.CharField(max_length=20)
    data_convite = models.DateField()
    asunto = models.TextField(max_length=500)
    dirije_ba = models.CharField(max_length=100)
    linha_ministerio = models.CharField(max_length=100)
    file_attachment = models.FileField(upload_to='karta_tama/')

    def __str__(self):
        return self.no_referensia

    class Meta:
        verbose_name = 'Convite Cafi'
        verbose_name_plural = 'Convite Cafi'
    
    def delete(self, *args, **kwargs):
        if self.file_attachment:
            os.remove(self.file_attachment.path)
        super().delete(*args, **kwargs)

class AgendaCafi(models.Model):
    no_karta = models.CharField(max_length=20, primary_key=True)
    no_referensia = models.CharField(max_length=20)
    data_reuniaun = models.DateField()
    data_sai = models.DateField()
    asunto = models.CharField(max_length=255)
    dirije_ba = models.CharField(max_length=100)
    linha_ministerio = models.CharField(max_length=100)
    file_attachment = models.FileField(upload_to='karta_sai/')

    def __str__(self):
        return self.no_referensia

    class Meta:
        verbose_name = 'Agenda Cafi'
        verbose_name_plural = 'Agenda Cafi'
    
    def delete(self, *args, **kwargs):
        if self.file_attachment:
            os.remove(self.file_attachment.path)
        super().delete(*args, **kwargs)