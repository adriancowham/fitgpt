from fitgptapi.models import Workout
from django.utils import timezone
from fitgptapi.services.fitbot import FitBotGPT

class WorkoutRepo():
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def today(self):
        return self.for_date(timezone.now().date())

    def for_date(self, date):
        workout = Workout.objects.filter(fitness_program=self.fitness_program, date=date).first()
        return FitBotGPT(self.fitness_program).new_workout(date) if workout is None else workout

