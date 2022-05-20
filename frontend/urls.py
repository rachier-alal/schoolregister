from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'scanners', views.ScannerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'scaner_records', views.ScannerRecordsViewSet)
