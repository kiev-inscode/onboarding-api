import django_filters

from django.db.models import Q,Count
from django.db.models.functions import Now

from datetime import datetime


class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr="icontains")
    idade = django_filters.NumberFilter()
    email = django_filters.CharFilter(lookup_expr="icontains")
    emprestimo_ativo = django_filters.BooleanFilter(method='emprestimo_ativo_filter')
    livro_emprestado = django_filters.CharFilter(
        field_name='emprestimos__livro__titulo',
        lookup_expr='icontains',
        distinct=True
    )
    atrasado = django_filters.BooleanFilter(method='atrasado_filter')

    def emprestimo_ativo_filter(self, queryset, name, value):
        queryset = queryset.annotate(
            emprestimos_ativos=Count('emprestimos', filter=Q(emprestimos__devolvido_em__isnull=True))
        )
        if value:
            return queryset.filter(emprestimos_ativos__gt=0)
        else:
            return queryset.filter(emprestimos_ativos=0)
        
    def atrasado_filter(self, queryset, name, value):
        queryset = queryset.annotate(
            emprestimos_atrasados=Count(
                'emprestimos',
                filter=Q(emprestimos__devolvido_em__isnull=True) & Q(emprestimos__vencimento_em__lt=Now()))
        )
        if value:
            return queryset.filter(emprestimos_atrasados__gt=0)
        else:
            return queryset.filter(emprestimos_atrasados=0)