from .models import FitnessProgram
from .models import FitnessProgramAudience
from .models import FitnessExperience
from .models import FitnessGoal

def boot():
  FitnessProgram.objects.get_or_create(
    audience=FitnessProgramAudience.INDIVIDUAL,
    goal=None,
    experience=FitnessExperience.INTERMEDIATE,
    user=None
  )
  FitnessProgram.objects.get_or_create(
    audience=FitnessProgramAudience.INDIVIDUAL,
    goal=FitnessGoal.ENDURANCE,
    experience=FitnessExperience.INTERMEDIATE,
    user=None
  )
  FitnessProgram.objects.get_or_create(
    audience=FitnessProgramAudience.INDIVIDUAL,
    goal=FitnessGoal.METCON,
    experience=FitnessExperience.INTERMEDIATE,
    user=None
  )
  FitnessProgram.objects.get_or_create(
    audience=FitnessProgramAudience.INDIVIDUAL,
    goal=FitnessGoal.BODYWEIGHT,
    experience=FitnessExperience.INTERMEDIATE,
    user=None
  )
  FitnessProgram.objects.get_or_create(
    audience=FitnessProgramAudience.AFFILIATE,
    goal=None,
    experience=FitnessExperience.INTERMEDIATE,
    user=None
  )