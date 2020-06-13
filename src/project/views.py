from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from accounts.models import Designation
from accounts.models import SiteUser
from accounts.models import Skill


def home(request):
    try:
        admin = SiteUser.objects.get(is_superuser=True)
    except SiteUser.DoesNotExist:
        return HttpResponse(
            "Super User object is not create create super user with 'python manage.py createsuperuser' command")
    else:
        user = admin
        skills = Skill.objects.filter(user=admin).order_by('position')
        designations = Designation.objects.filter(user=admin)
        designation = ""
        for i in designations:
            designation += f"{i.name},"

        count = 0
        count_type = " "
        if user.experience_from:
            time = user.experience_from
            today = timezone.now()
            difference = today - time
            difference = difference.days
            year = difference / 365
            year = int(year)
            count = year
            count_type = "years"
            print(year)
            if year == 0:
                count = int(difference / 30)
                count_type = "months"
        experience = {
            "count": count,
            "type": count_type
        }

    context = {
        "admin": user,
        "skills": skills,
        "designation": designation,
        "experience": experience
    }
    return render(request, 'home/home.html', context)
