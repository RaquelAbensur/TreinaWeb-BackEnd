from rest_framework.views import APIView
from rest_framework.response import Response

class HomeAPIView(APIView):
    def get(self, request, format=None):
        return Response({"nome": "Gustavo Bardini", "idade": 18}, status=200)