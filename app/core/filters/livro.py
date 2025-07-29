import django_filters
from django.db.models import Q, Count

import logging

logger = logging.getLogger()

class LivroFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr="icontains")
    autor = django_filters.CharFilter(lookup_expr="icontains")
    editor = django_filters.CharFilter(lookup_expr="icontains")
    publicado_em = django_filters.DateFromToRangeFilter()
    is_emprestado = django_filters.BooleanFilter(method='emprestado_filter')

    def emprestado_filter(self, queryset, name, value):
        queryset = queryset.annotate(
            emprestimos_ativos=Count('emprestimos', filter=Q(emprestimos__devolvido_em__isnull=True))
        )
        if value:
            return queryset.filter(emprestimos_ativos__gt=0)
        else:
            return queryset.filter(emprestimos_ativos=0)