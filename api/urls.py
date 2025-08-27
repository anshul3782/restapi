from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from simple_api import get_phone_data

@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "API is working!", 
        "endpoints": ["/data/{phone_number}/"],
        "status": "ready"
    })

urlpatterns = [
    path("", api_root),
    path("data/<str:phone_number>/", get_phone_data, name="phone_data"),
    path("admin/", admin.site.urls),
    path("api/", include("checkins.urls")),
]
