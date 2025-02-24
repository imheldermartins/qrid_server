# from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from services.serializers import ServiceSerializer

from .models import Service


# def service_list(req):

#     services = Service.objects.all()

#     response = {"services": services}
#     return render(req, "services/service_list.html", response)


@api_view(["GET"])
def get_services(req):
    if req.method == "GET":
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
