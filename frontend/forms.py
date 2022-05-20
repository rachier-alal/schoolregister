import django_filters

from students.models import Student


class NullFilter(django_filters.BooleanFilter):
    """Filter on a field set as null or not."""
    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class StudentFilter(django_filters.FilterSet):
    backlog = NullFilter(name='student')
    class Meta:
        model = Student
        fields = ('name', 'rfid_code','slug','author', 'backlog')