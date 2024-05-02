from django.utils.crypto import get_random_string
from rest_framework import serializers
from authentication.serializers import UserSerializer

from .models import (
    ProGroup,
    ProGroupUser,
    Schedule,
    Session,
    SessionUser,
    Offense,
    OffenseUser,
)


class ProGroupSerializer(serializers.ModelSerializer):
    users_count = serializers.IntegerField(read_only=True)
    code = serializers.CharField(read_only=True)

    class Meta:
        model = ProGroup
        exclude = ('users',)

    def create(self, validated_data):
        ok = True
        code = None
        while ok:
            code = get_random_string(6).upper()
            ok = ProGroup.objects.filter(code=code).exists()
        validated_data['code'] = code
        return super().create(validated_data)


class ProGroupUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()

    class Meta:
        model = ProGroupUser
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class SessionUserSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(required=False)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField()

    class Meta:
        model = SessionUser
        fields = '__all__'

    def create(self, validated_data: dict):
        session_id = validated_data.get('session')
        c = SessionUser.objects.filter(session=session_id).count()
        validated_data['order'] = c + 1
        return super().create(validated_data)


class OffenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offense
        fields = '__all__'


class OffenseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffenseUser
        fields = '__all__'
