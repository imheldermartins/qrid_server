from django.shortcuts import render

from .models import Service


def service_list(req):

    services = Service.objects.all()

    response = {"services": services}
    return render(req, "services/service_list.html", response)
