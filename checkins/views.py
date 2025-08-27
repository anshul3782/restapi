from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CheckinData
from .serializers import CheckinDataSerializer

class CheckinDataViewSet(viewsets.ModelViewSet):
    queryset = CheckinData.objects.all()
    serializer_class = CheckinDataSerializer

    def get_queryset(self):
        queryset = CheckinData.objects.all()
        phone = self.request.query_params.get('phone')
        if phone:
            queryset = queryset.filter(phone_number=phone)
        return queryset

    @action(detail=False, url_path='by-phone/(?P<number>[^/.]+)')
    def by_phone(self, request, number=None):
        checkins = CheckinData.objects.filter(phone_number=number)
        serializer = self.get_serializer(checkins, many=True)
        return Response(serializer.data)
