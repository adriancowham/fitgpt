import json
from django.utils import timezone

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from munch import DefaultMunch as munch
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from fitgptapi.models import FitnessProgram, Workout, FitnessProgramAudience, FitnessGoal
from fitgptapi.serializers import FitnessProgramSerializer
from fitgptapi.services.social.google import Google
from rest_framework.views import APIView
from django.utils import timezone
from fitgptapi.repos import WorkoutRepo

class DefaultIndividualView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        dateParam = self.request.GET.get('date')
        date = timezone.now().date()
        if dateParam is not None:
            date = timezone.datetime.strptime(dateParam, "%Y-%m-%d").date()
        fitness_program = FitnessProgram.objects.get(user=None, goal=None, audience=FitnessProgramAudience.INDIVIDUAL)
        workout = WorkoutRepo(fitness_program).for_date(date)
        # workout = Workout.objects.filter(fitness_program=fitness_program, date=date).first()
        if workout is None:
            return JsonResponse({"error_description": f"No workout for date {date}"}, status=400)
        return JsonResponse({"content": workout.content, "date": workout.date})

class DefaultIndividualEnduranceView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        dateParam = self.request.GET.get('date')
        date = timezone.now().date()
        if dateParam is not None:
            date = timezone.datetime.strptime(dateParam, "%Y-%m-%d").date()
        fitness_program = FitnessProgram.objects.get(user=None, goal=FitnessGoal.ENDURANCE, audience=FitnessProgramAudience.INDIVIDUAL)
        workout = WorkoutRepo(fitness_program).for_date(date)
        # workout = Workout.objects.filter(fitness_program=fitness_program, date=date).first()
        if workout is None:
            return JsonResponse({"error_description": f"No workout for date {date}"}, status=400)
        return JsonResponse({"content": workout.content, "date": workout.date})

class DefaultIndividualMetconView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        dateParam = self.request.GET.get('date')
        date = timezone.now().date()
        if dateParam is not None:
            date = timezone.datetime.strptime(dateParam, "%Y-%m-%d").date()
        fitness_program = FitnessProgram.objects.get(user=None, goal=FitnessGoal.METCON, audience=FitnessProgramAudience.INDIVIDUAL)
        workout = WorkoutRepo(fitness_program).for_date(date)
        # workout = Workout.objects.filter(fitness_program=fitness_program, date=date).first()
        if workout is None:
            return JsonResponse({"error_description": f"No workout for date {date}"}, status=400)
        return JsonResponse({"content": workout.content, "date": workout.date})

class DailyAffiliateView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        dateParam = self.request.GET.get('date')
        date = timezone.now().date()
        if dateParam is not None:
            date = timezone.datetime.strptime(dateParam, "%Y-%m-%d").date()
        fitness_program = FitnessProgram.objects.get(user=None, audience=FitnessProgramAudience.AFILIATE)
        workout = WorkoutRepo(fitness_program).for_date(date)
        if workout is None:
            return JsonResponse({"error_description": f"No workout for date {date}"}, status=400)
        return JsonResponse({"content": workout.content, "date": workout.date})

class DefaultIndividualBodyWeightView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        dateParam = self.request.GET.get('date')
        date = timezone.now().date()
        if dateParam is not None:
            date = timezone.datetime.strptime(dateParam, "%Y-%m-%d").date()
        fitness_program = FitnessProgram.objects.get(user=None, goal=FitnessGoal.BODYWEIGHT, audience=FitnessProgramAudience.INDIVIDUAL)
        workout = WorkoutRepo(fitness_program).for_date(date)
        if workout is None:
            return JsonResponse({"error_description": f"No workout for date {date}"}, status=400)
        return JsonResponse({"content": workout.content, "date": workout.date})

class FitnessProgramViewSet(viewsets.ModelViewSet, APIView):
  queryset = FitnessProgram.objects.all()
  serializer_class = FitnessProgramSerializer

class SocialLoginView(View):
    # Parse JSON body and return a token if the user exists
    def post(self, request, *args, **kwargs):
        # Parse the request body
        json_body = munch.fromDict(json.loads(request.body))
        user_profile = json_body.profile
        # Get the provider we're using
        provider = json_body.provider
        # Validate the Google access token
        user = Google(user_profile).get_user()
        if(user is None):
            return JsonResponse({"error": "Invalid token"}, status=400)

        # Create User if it doesn't exist
        user_model, _ = User.objects.get_or_create(
            username=user.email,
            email=user.email,
            defaults={
              'first_name': user.first_name,
              'last_name': user.last_name,
              'date_joined': timezone.now(),
              'is_active': True})

        # Create token for user
        token, _ = Token.objects.get_or_create(user=user_model)
        return JsonResponse({"token": token.key}, status=200)