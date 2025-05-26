from datetime import timedelta
from django.utils.timezone import localtime

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
DEFAULT_LONG_VISIT_MINUTES = 60


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f'{hours}ч {minutes}мин'


def get_duration(visit):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at
    return localtime() - visit.entered_at


def is_visit_long(visit, minutes=DEFAULT_LONG_VISIT_MINUTES):
    return get_duration(visit) > timedelta(minutes=minutes)
