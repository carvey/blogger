__author__ = 'charles'
import datetime
import pytz
from django import template
from pytz import timezone

register = template.Library()

@register.filter(name='adjust_time')
def adjust_time(time):
    eastern = timezone('US/Eastern')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    loc_dt = eastern.localize(time)
    return time