from django.core.management.base import BaseCommand, CommandError
from api.models import Time_Period,User_Name
import random
from django.utils import timezone
from api.models import Time_Period,User_Name
from faker import Faker
import pytz
fake = Faker()

time_material = []
for tz in pytz.all_timezones:
    time_material.append(tz)

def create_data(N):
    fake = Faker()

    for i in range(N):
        user_name = fake.name()
        user_object = User_Name.objects.get_or_create(real_name = user_name,timezone = random.choice(time_material))[0]
        for i in range(3):
            start_time = timezone.now()
            end_time = timezone.now()
            date_time_object = Time_Period.objects.get_or_create(start_time = start_time,end_time = end_time, user_name = user_object )[0]

class Command(BaseCommand):
    help = 'populate the data uing Faker library '

    # def add_arguments(self, parser):
    #     parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        create_data(10)
        self.stdout.write(self.style.SUCCESS('Successfully created dummy data '))
