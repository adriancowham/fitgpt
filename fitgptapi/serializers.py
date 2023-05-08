from rest_framework import serializers
from .models import FitnessProgram, FitnessGoal, User

class FitnessProgramSerializer(serializers.ModelSerializer):
  class Meta:
    model = FitnessProgram
    fields = ['id', 'audience', 'fitness_goal']