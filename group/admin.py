from django.contrib import admin
from .models import (
    ProGroup,
    ProGroupUser,
    Schedule,
    Session,
    SessionUser,
    Offense,
)

admin.site.register(ProGroup)
admin.site.register(ProGroupUser)
admin.site.register(Schedule)
admin.site.register(Session)
admin.site.register(SessionUser)
admin.site.register(Offense)
