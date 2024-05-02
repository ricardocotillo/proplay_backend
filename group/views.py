from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.db.models import Count
from django.db.models.functions import Coalesce
from .models import (
    ProGroup,
    ProGroupUser,
    Schedule,
    Session,
    SessionUser,
)
from .serializers import (
    ProGroupSerializer,
    ProGroupUserSerializer,
    ScheduleSerializer,
    SessionSerializer,
    SessionUserSerializer,
)


class ProGroupViewSet(viewsets.ModelViewSet):
    queryset = ProGroup.objects.annotate(
        users_count=Coalesce(Count('users', ), 0),
    ).order_by('-created')
    serializer_class = ProGroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('users',)


class ProGroupUserViewSet(viewsets.ModelViewSet):
    queryset = ProGroupUser.objects.order_by('-created')
    serializer_class = ProGroupUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('group', 'user')


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.order_by('-created')
    serializer_class = ScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('progroup',)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.order_by('-date')
    serializer_class = SessionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('schedule',)


class SessionUserViewSet(viewsets.ModelViewSet):
    queryset = SessionUser.objects.order_by('order')
    serializer_class = SessionUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('session', 'user',)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
