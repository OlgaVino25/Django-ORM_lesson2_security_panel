from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .visit_duration_utils import format_duration, is_visit_long, get_duration


def storage_information_view(request):
    current_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in current_visits:
        duration = get_duration(visit)

        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at).strftime("%d-%m-%Y %H:%M"),
                'duration': format_duration(duration),
                "is_strange": is_visit_long(visit)
            } 
        )


    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)