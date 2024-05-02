from django_seed import Seed
from django_seed.seeder import Seeder
from django.core.management.base import BaseCommand, CommandError
from authentication.models import User
from group.models import ProGroup, ProGroupUser


class Command(BaseCommand):
    seeder: Seeder = Seed.seeder()

    def handle(self, *args, **options):
        for i in range(10):
            User.objects.create_user(
                username=self.seeder.faker.name(),
                email=self.seeder.faker.email(),
                password='123456',
                first_name=self.seeder.faker.first_name(),
                last_name=self.seeder.faker.last_name(),
            )

        users = User.objects.all()
        for u in users:
            group = ProGroup.objects.create(
                name=self.seeder.faker.name(),
            )
            group.users.add(*users)
            progroup_user = ProGroupUser.objects.get(user=u, group=group)
            progroup_user.role = ProGroupUser.Roles.ADMIN
            progroup_user.save()
