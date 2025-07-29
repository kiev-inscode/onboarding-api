import django_filters


class EmprestimoFilter(django_filters.FilterSet):
    livro = django_filters.CharFilter(
        field_name="livro__titulo",
        lookup_expr="icontains"
    )
    usuario = django_filters.CharFilter(
        field_name="usuario__nome",
        lookup_expr="icontains"
    )
    emprestado_em = django_filters.DateFromToRangeFilter()
    vencimento_em = django_filters.DateFromToRangeFilter()
    devolvido_em = django_filters.DateFromToRangeFilter()

    ativo = django_filters.BooleanFilter(
        field_name="devolvido_em",
        lookup_expr="isnull"
    )

