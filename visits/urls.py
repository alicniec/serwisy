from rest_framework.routers import DefaultRouter
from visits.views import VisitViewSet

router = DefaultRouter()

router.register(r'visits', VisitViewSet, basename='visits')
