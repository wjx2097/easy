from django.db import models

# Create your models here.
class   host(models.Model):
    hostname = models.CharField(max_length=50, verbose_name='主机')

    class  Meta:
        db_table ="Host"
        verbose_name="服务器"
        verbose_name_plural = '服务器'


    def __str__(self):
        return self.hostname