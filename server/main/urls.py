from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignUpView, SignInView, CourseViewSet, AssessmentViewSet, GradeViewSet
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'assessment', AssessmentViewSet, basename='assessment')
router.register(r'grade', GradeViewSet, basename='grade')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', SignUpView.as_view(), name='Sign Up'),
    path('sign-in/', SignInView.as_view(), name='Sign In'), 
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
