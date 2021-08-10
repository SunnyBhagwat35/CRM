from django.db.models import fields
import django_filters
from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label="From Date")
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='To Date')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
        field_labels={
            'username': 'User account',
        }