from rest_framework import routers
from .views import (
    ProGroupViewSet,
    ProGroupUserViewSet,
    ScheduleViewSet,
    SessionViewSet,
    SessionUserViewSet,
)

router = routers.SimpleRouter()

router.register(r'progroups', ProGroupViewSet)
router.register(r'progroup-users', ProGroupUserViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'session-users', SessionUserViewSet)

urlpatterns = router.urls
