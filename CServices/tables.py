import django_tables2 as tables
from .models import WipReq


class WiplogTable(tables.Table):
    class Meta:
        model = WipReq
        attrs = {'class': 'paleblue'}
