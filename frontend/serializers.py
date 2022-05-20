from django.contrib.auth import get_user_model
from rest_framework import serializers
from students.models import Student
from biometrics.models import ScannerRecords, Scanners
from rest_framework.reverse import reverse
from .views import *

User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = Student
        fields = ('name', 'rfid_code','slug','author', 'links',)

    def get_links(self,obj):
        request = self.context['request']
        return{
            'self':reverse('student-detail',
            kwargs={'pk': obj.pk},
            request=request),

        }
        if obj.student_id:
            links['author_id'] = reverse('user-detail',
            kwargs={'pk': obj.author_id}, request=request)



class ScannerSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model =  Scanners
        fields = ('room', 'slug', 'links',)

    def get_links(self,obj):
        request = self.context['request']
        return{
            'self':reverse('scanners-detail',
            kwargs={'pk': obj.pk},
            request=request),

        }
        

class ScannerRecordsSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    class Meta:
        model = ScannerRecords
        fields = ('student', 'room', 'updated_at','links',)

    def get_links(self,obj):
        request = self.context['request']
        return{
            'self':reverse('scannerrecords-detail',
            kwargs={'pk': obj.pk},
            request=request),
            'student':reverse('student-detail',
            kwargs={'pk':obj.student.id},
            request=request),
            'room':reverse('scanners-detail',
            kwargs={'pk':obj.room.id},
            request=request
            ),
        }
        if obj.student:
            links['student'] = reverse('student-detail',
            kwargs={'pk': obj.sprint_id}, request=request)
        if obj.room_id:
            links['room_id'] = reverse('scanners-detail',
            kwargs={'pk': obj.room_id}, request=request)


class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active','links', )

    def get_links(self, obj): 
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail',
            kwargs={User.USERNAME_FIELD: username}, request=request),
        }
