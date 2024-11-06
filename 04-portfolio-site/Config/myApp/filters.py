# import django_filters
# from .models import MaqolaModel
#
# class ProjectFilter(django_filters.FilterSet):
#     class Meta:
#         model = MaqolaModel
#         fields = ['title', 'tags']  # Add other fields as needed


# ------------------------------------------------------------

import django_filters
from django.db.models import Q
from .models import MaqolaModel

# class ProjectFilter(django_filters.FilterSet):
#     search = django_filters.CharFilter(method='filter_by_all', label='Search (q object)')
#
#     class Meta:
#         model = MaqolaModel
#         fields = ['title', 'tags']
#
#     def filter_by_all(self, queryset, name, value):
#         return queryset.filter(
#             Q(title__icontains=value) |
#             Q(tags__icontains=value)
#         )

import django_filters
from .models import MaqolaModel
from django.db.models import Q

class ProjectFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_all', label='Search (q object)')
    class Meta:
        model = MaqolaModel
        fields = ['title', 'tags']

    def filter_by_all(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(tags__icontains=value)
        )