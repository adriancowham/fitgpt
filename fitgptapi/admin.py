from django.contrib import admin

# Register your models here.
from .models import FitnessProgram, Workout, Prompt

admin.site.register(FitnessProgram)
admin.site.register(Workout)
admin.site.register(Prompt)

