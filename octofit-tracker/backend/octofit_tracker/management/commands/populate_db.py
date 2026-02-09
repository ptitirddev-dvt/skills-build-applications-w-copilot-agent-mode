from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=date(2024, 1, 1))
        Activity.objects.create(user=steve, type='pushup', duration=20, date=date(2024, 1, 2))
        Activity.objects.create(user=bruce, type='run', duration=40, date=date(2024, 1, 3))
        Activity.objects.create(user=clark, type='pushup', duration=25, date=date(2024, 1, 4))

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=100, rank=3)
        Leaderboard.objects.create(user=clark, score=90, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
