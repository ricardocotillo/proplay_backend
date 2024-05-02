from model_utils.models import TimeStampedModel
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.db import models


class ProGroup(TimeStampedModel):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True)
    code = models.CharField(max_length=10, unique=True)
    users = models.ManyToManyField(
        'authentication.User',
        related_name='progroups',
        through='group.ProGroupUser',
    )


class ProGroupUser(TimeStampedModel):
    class Roles(models.TextChoices):
        OWNER = 'owner', 'Owner'
        ADMIN = 'admin', 'Admin',
        MEMBER = 'member', 'Member'

    group = models.ForeignKey(
        'group.ProGroup',
        on_delete=models.CASCADE,
        related_name='progroup_users',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='progroup_users',
    )
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.MEMBER,
    )


class Schedule(TimeStampedModel):
    progroup = models.ForeignKey(
        'group.ProGroup',
        on_delete=models.CASCADE,
        related_name='schedules',
    )
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
    )
    open_day = models.PositiveBigIntegerField()
    open_time = models.TimeField()
    day = models.PositiveIntegerField(
        validators=[MaxValueValidator(6)]
    )
    time = models.TimeField()
    number_of_players = models.PositiveBigIntegerField()


class Session(TimeStampedModel):
    schedule = models.ForeignKey(
        'group.Schedule',
        on_delete=models.CASCADE,
        related_name='sessions',
    )
    amount = models.DecimalField(
        null=True,
        max_digits=6,
        decimal_places=2,
    )
    address = models.CharField(max_length=500)
    date = models.DateTimeField()
    users = models.ManyToManyField(
        'authentication.User',
        related_name='sessions',
        through='group.SessionUser'
    )


class SessionUser(TimeStampedModel):
    session = models.ForeignKey(
        'group.Session',
        on_delete=models.CASCADE,
        related_name='session_users',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='session_users',
    )
    order = models.PositiveIntegerField()
    paid = models.BooleanField(default=False)
    assisted = models.BooleanField(default=False)
    late = models.BooleanField(default=False)


class Offense(TimeStampedModel):
    class Punishment(models.TextChoices):
        SUSPENSION = 'suspension', 'Suspension',
    progroup = models.ForeignKey(
        'group.ProGroup',
        on_delete=models.CASCADE,
        related_name='offenses'
    )
    name = models.CharField(max_length=250)
    time = models.PositiveIntegerField(null=True)  # in hours
    sessions = models.PositiveIntegerField(null=True)


class OffenseUser(TimeStampedModel):
    offense = models.ForeignKey(
        'group.Offense',
        on_delete=models.CASCADE,
        related_name='offense_users',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='offense_users',
    )
    date = models.DateTimeField(default=timezone.now)
    time = models.PositiveIntegerField(null=True)  # in hours
    sessions = models.PositiveIntegerField(null=True)
