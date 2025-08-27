from rest_framework.decorators import api_view
from rest_framework.response import Response

# Simple hardcoded data for testing
test_data = {
    "1111111111": {"phone": "1111111111", "steps": 100, "heart_rate": 65, "mood": "Good"},
    "2222222222": {"phone": "2222222222", "steps": 200, "heart_rate": 70, "mood": "Great"},
}

@api_view(['GET'])
def get_phone_data(request, phone_number):
    """Simple endpoint to get data by phone number"""
    data = test_data.get(phone_number)
    if data:
        return Response(data)
    else:
        return Response({"error": "Phone number not found"}, status=404)
