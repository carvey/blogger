__author__ = 'charles'
import datetime
from django import template
from pytz import timezone

register = template.Library()

@register.filter(name='adjust_time')
def adjust_time(time)
    eastern = timezone('US/Eastern')