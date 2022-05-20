from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, generics
import django_filters.rest_framework as filters
from rest_framework import filters as rf
from students.models import Student
from biometrics.models import Scanners, ScannerRecords
from .serializers import StudentSerializer, ScannerRecordsSerializer, UserSerializer, ScannerSerializer
from .views import StudentFilter

User = get_user_model()

class DefaultsMixin(object): 
    """Default settings for view authentication, permissions,filtering and pagination."""
    authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = ( 
        filters.DjangoFilterBackend,
        rf.SearchFilter,
        rf.OrderingFilter,
        )


class StudentViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset= Student.objects.order_by('slug')
    serializer_class = StudentSerializer
    filter_class = StudentFilter
    search_fields = ('name', )
    ordering_fields = ('name', ) 


class ScannerViewSet(DefaultsMixin,  viewsets.ModelViewSet):
    queryset = Scanners.objects.all()
    serializer_class = ScannerSerializer
    ordering_fields = ('room', ) 


class ScannerRecordsViewSet(DefaultsMixin,  viewsets.ModelViewSet):
    queryset = ScannerRecords.objects.all()
    serializer_class = ScannerRecordsSerializer
    ordering_fields = ('updated_at',  ) 


class UserViewSet(DefaultsMixin,  viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    
