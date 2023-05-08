from fitgptapi.models import Prompt, PromptRole, FitnessProgramAudience, FitnessGoal
from django.utils import timezone
from django.db.models import Max

def builder_for(fitness_program):
    if fitness_program.audience == FitnessProgramAudience.AFFILIATE:
        return AffiliatePromptBuilder(fitness_program)

    if fitness_program.audience == FitnessProgramAudience.INDIVIDUAL:
        if fitness_program.goal == FitnessGoal.ENDURANCE:
            return EndurancePromptBuilder(fitness_program)
        if fitness_program.goal == FitnessGoal.METCON:
            return MetconPromptBuilder(fitness_program)
        if fitness_program.goal == FitnessGoal.BODYWEIGHT:
            return BodyWeightPromptBuilder(fitness_program)

    return GeneralPromptBuilder(fitness_program)

class BasePromptBuilder():
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def build(self):
        initial_prompts = self.get_initial_prompts()
        max_sequence_num = initial_prompts.aggregate(Max('sequence_num'))['sequence_num__max']
        self.next_prompt()
        recent_prompts = self.fitness_program.prompt_set.filter(sequence_num__gt=max_sequence_num).order_by('-sequence_num').all()
        recent_prompts = reversed(recent_prompts[:10])
        return list(recent_prompts) + list(initial_prompts)

    def get_initial_prompts(self):
        initial_prompts = self.initial_prompts()
        if initial_prompts.count() == 0:
          initial_prompts = self.create_initial_prompts()
        return initial_prompts

    def initial_prompts(self):
        return self.fitness_program.prompt_set.order_by('sequence_num').all()[:2]

    def create_initial_prompts(self):
        self.system_prompt()
        self.intro_prompt()
        return self.initial_prompts()

    def system_prompt(self):
        prompt = Prompt(
            role=PromptRole.SYSTEM,
            content="You are a helpful and knowledgeable CrossFit Coach. You are here to help your client achieve their fitness goals. When prompted, you will create a workout that is either an AMRAP, EMOM, rounds for time, or a chipper, but never the same one twice in a row. The workout will no shorter than 10 minutes and no longer than 30 minutes. You will format the workout as HTML wrapped in a <div> tag. You will not include a name or title for the workout. You will not include a cooldown. You will not include a warm-up.",
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

    def save_response(self, message):
        prompt = Prompt(
            role=PromptRole.ASSISTANT,
            content=message,
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

    def next_sequence_num(self):
        return self.fitness_program.prompt_set.count()

    def intro_prompt(self):
        return None

    def instructions(self):
        return ""

    def next_prompt(self):
        last_prompt = self.fitness_program.prompt_set.order_by('-sequence_num').first()
        if last_prompt.role == PromptRole.USER:
            return None

        prompt = Prompt(
            role=PromptRole.USER,
            content="I completed that workout, can you create another workout that has a different time domain and format that the previous 3 workouts?" + self.instructions(),
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

class AffiliatePromptBuilder(BasePromptBuilder):
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def intro_prompt(self):
        prompt = Prompt(
            role=PromptRole.USER,
            content="Can you create a unique workout for my class of 15 athletes? " + self.instructions(),
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

class EndurancePromptBuilder(BasePromptBuilder):

    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def intro_prompt(self):
        prompt = Prompt(
            role=PromptRole.USER,
            content="I have acces to a gym with all types of equipment and I'd like to improve my endurance. Can you create a workout for me? " + self.instructions(),
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

class MetconPromptBuilder(BasePromptBuilder):

    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def intro_prompt(self):
        prompt = Prompt(
            role=PromptRole.USER,
            content="I have acces to a gym with all types of equipment and I'd like to improve my metabolic conditioning. Can you create a workout for me? " + self.instructions(),
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

class GeneralPromptBuilder(BasePromptBuilder):
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def intro_prompt(self):
        prompt = Prompt(
            role=PromptRole.USER,
            content="I have access to a gym with all types of equipment, can you create a workout for me? " + self.instructions() + " Do not include a strength component.",
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt

class BodyWeightPromptBuilder(BasePromptBuilder):
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program

    def intro_prompt(self):
        prompt = Prompt(
            role=PromptRole.USER,
            content="I don't have any equipment. Can you create a workout for me? " + self.instructions(),
            prompted_at=timezone.now(),
            prompted_on=timezone.now().date(),
            sequence_num=self.next_sequence_num(),
            fitness_program=self.fitness_program
        )
        prompt.save()
        return prompt