from django.urls import include, path
from rest_framework import routers
from nodos.nodo import views

router = routers.DefaultRouter()
router.register(r'vehicle_type', views.VehicleTypeViewSet)
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'journey', views.JourneyViewSet)
router.register(r'service_area', views.ServiceAreaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]