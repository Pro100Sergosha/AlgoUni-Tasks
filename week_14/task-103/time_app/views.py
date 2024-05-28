from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils.timezone import datetime

class TimeViewerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({'current_time': datetime.now()})