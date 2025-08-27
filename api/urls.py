from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request):
    return Response({"message": "API is working!", "endpoints": ["/api/checkins/"]})

urlpatterns = [
    path("", api_root),
    path("admin/", admin.site.urls),
    path("api/", include("checkins.urls")),
]
