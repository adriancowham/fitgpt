from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SocialLoginView
from .views import DefaultIndividualView, DefaultIndividualEnduranceView, DefaultIndividualMetconView, DailyAffiliateView, DefaultIndividualBodyWeightView

router = routers.DefaultRouter()
router.register(r'fitnessprograms', views.FitnessProgramViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('individual/', DefaultIndividualView.as_view()),
    path('individual/endurance/', DefaultIndividualEnduranceView.as_view()),
    path('individual/metcon/', DefaultIndividualMetconView.as_view()),
    path('individual/bodyweight/', DefaultIndividualBodyWeightView.as_view()),
    path('affiliate/', DailyAffiliateView.as_view()),
    path('social/login/', SocialLoginView.as_view()),
]