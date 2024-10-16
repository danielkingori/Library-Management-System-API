import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', required=False)
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', required=False)
    isbn = django_filters.CharFilter(lookup_expr='exact', required=False)
    available = django_filters.BooleanFilter(method='filter_available', label='Available')

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available']
       
    def filter_available(self, queryset, name, value):
        if value:  # If the value is True, filter for books with at least 1 available copy
            return queryset.filter(number_of_copies_available__gt=0)
        return queryset  # If False or not provided, return the full queryset