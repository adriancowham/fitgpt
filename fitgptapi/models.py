from django.db import models
from django.contrib.auth.models import User

FitnessProgramAudience = models.TextChoices('FitnessProgramAudience', 'INDIVIDUAL AFFILIATE GLOBAL')
FitnessExperience = models.TextChoices('FitnessExperience', 'BEGINNER INTERMEDIATE ADVANCED PROFESSIONAL')
FitnessGoal = models.TextChoices('FitnessGoal', 'ENDURANCE METCON BODYWEIGHT')
WorkoutScale = models.TextChoices('WorkoutScale', 'RX SCALED')
PromptRole = models.TextChoices('PromptRole', 'SYSTEM USER ASSISTANT')

class UserAccountInfo():
  def __init__(self, first_name, last_name, email):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

class FitnessProgram(models.Model):
  audience = models.CharField(max_length=255, choices=FitnessProgramAudience.choices, default=FitnessProgramAudience.INDIVIDUAL, null=True, blank=True)
  goal = models.CharField(max_length=255, choices=FitnessGoal.choices, default=None, null=True, blank=True)
  experience = models.CharField(max_length=255, choices=FitnessExperience.choices, default=None, null=True, blank=True)
  # FitnessPrograms can have one user
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self):
    return self.audience

class Workout(models.Model):
  fitness_program = models.ForeignKey(FitnessProgram, on_delete=models.CASCADE, null=True)
  date = models.DateField(null=True)
  content = models.TextField(null=True)
  scale = models.CharField(max_length=255, choices=WorkoutScale.choices, default=WorkoutScale.RX, null=False, blank=False)
  def __str__(self):
    return self.date.strftime("%m/%d/%Y")

class Prompt(models.Model):
  role = models.CharField(max_length=255, choices=PromptRole.choices, null=True)
  content = models.TextField(null=True)
  prompted_at = models.DateTimeField(null=True)
  prompted_on = models.DateField(null=True)
  sequence_num = models.IntegerField(null=True)
  fitness_program = models.ForeignKey(FitnessProgram, on_delete=models.CASCADE, null=True)

  def to_message(self):
    return {"role": self.role.lower(), "content": self.content}

  def __str__(self):
    return self.content