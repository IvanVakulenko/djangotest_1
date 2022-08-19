from django.db import models

# Create your models here.

class PriceCard(models.Model):
    pc_value = models.CharField(max_length=20, verbose_name = 'Price')
    pc_description = models.CharField(max_length=200, verbose_name = 'Description')

    def __str__(self):
        return self.pc_value
    
class Meta:
    verbose_name = 'Service'
    verbose_name_plural = 'Services'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name = 'Service')
    pt_old_price = models.CharField(max_length=200, verbose_name = 'Old Price')
    pt_new_price = models.CharField(max_length=200, verbose_name = 'New Price')
    
    