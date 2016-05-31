import django_tables2 as tables
from .models import WipReq


class WiplogTable(tables.Table):

    class SummingColumn(tables.Column):
        def render_footer(self, bound_column, table):
            return sum(bound_column.accessor.resolve(row) for row in table.data)
    
    class Meta:
        model = WipReq
        attrs = {
            'th' : {
                '_ordering': {
                    'orderable': 'sortable',
                    'ascending': 'ascend',
                    'descending': 'descend'
                    }
                }
            }
    name = tables.Column()
    size = tables.Column(footer='Total:')
    cost = SummingColumn()
    
    
        
