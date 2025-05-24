from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecialistViewSet, QualificationCourseViewSet, ParticipationViewSet

router = DefaultRouter()
router.register(r'specialists', SpecialistViewSet)
router.register(r'courses', QualificationCourseViewSet)
router.register(r'participation', ParticipationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from .views import participation_chart

urlpatterns += [
    path('participation_chart/', participation_chart, name='participation_chart'),
]