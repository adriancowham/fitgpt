from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from fitgptapi.models import Prompt