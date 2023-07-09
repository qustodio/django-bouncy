"""Signals from the django_bouncy app"""
# pylint: disable=invalid-name
from django.dispatch import Signal

# Any notification received
notification = Signal()

# New SubscriptionConfirmation received
subscription = Signal()

# New bounce or complaint received
feedback = Signal()
