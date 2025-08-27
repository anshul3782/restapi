from rest_framework import serializers
from .models import CheckinData

class CheckinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckinData
        fields = "__all__"
