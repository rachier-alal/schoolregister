# from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from frontend.urls import router

urlpatterns = [
    path('api/token/', obtain_auth_token, name= 'api_token'),
    path('api/', include(router.urls), name= 'api'),
    path('', include(router.urls), name= 'api'),
    # url(r'^api/token/',obtain_auth_token, name= 'api_token'),
]
