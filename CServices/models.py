from django.db import models
from django.utils import timezone

METHS = (('PHONE', 'phone'),
         ('ONLINE', 'online'),
         ('QUAL', 'qual'),
         ('ROOM', 'room'))


class WipReq(models.Model):


    
    author  = models.ForeignKey('auth.User')
    name    = models.CharField(max_length=30)
    bid     = models.FloatField()
    length  = models.IntegerField()
    size    = models.IntegerField()
    cost    = models.IntegerField()
    meth    = models.CharField(choices=METHS,
                               max_length=20,
                               null=True,
                               verbose_name='method')
    date    = models.DateTimeField(
        blank=True, null=True)

    def final(self):
        self.save()

    def __str__(self):
        return self.name
