import openai
from fitgptapi.models import Prompt, PromptRole, Workout
from django.utils import timezone
from fitgptapi.builders import builder_for
from bs4 import BeautifulSoup as soup

openai.api_key = ""

class FitBotGPT():
    def __init__(self, fitness_program):
        self.fitness_program = fitness_program
        self.builder = builder_for(fitness_program)

    def new_workout(self, date):
        messages = list(map(lambda prompt: prompt.to_message(), self.builder.build()))

        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages)
        message = response['choices'][0]['message']['content']
        self.builder.save_response(message)
        return self.save_workout(message, date)

    def save_workout(self, message, date):
        first_index = message.find('<div>')
        last_index = message.find('</div>')
        content = message[first_index:last_index]
        workout = Workout(
            date=date,
            content=content,
            fitness_program=self.fitness_program
        )
        workout.save()
        return workout

