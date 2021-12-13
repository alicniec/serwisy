from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from visits.serializers import VisitSerializer
from .models import Visit


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    @action(detail=True, methods=['post'])
    def register(self, request, pk):
        obj = self.get_object()
        obj.patient = request.user
        obj.save()
        return Response(status=201)
