from .models import VehicleType, Vehicle, Journey, ServiceArea
from rest_framework import viewsets
from rest_framework import permissions
from nodos.nodo.serializers import VehicleTypeSerializer, VehicleSerializer, JourneySerializer, ServiceAreaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class VehicleTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VehicleType.objects.all().order_by('name')
    serializer_class = VehicleTypeSerializer
    permission_classes = [permissions.AllowAny]

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.AllowAny]

class JourneyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.AllowAny]

class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.AllowAny]

    #realiza búsqueda de arriba hacia abajo o de abajo hacia arriba
    @action(detail=False)
    def get_route_beta(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        response = []

        node_a = ServiceArea.objects.get(kilometer=a)
        node_b = ServiceArea.objects.get(kilometer=b)

        curr_node = node_a
        if curr_node:
            response.append({
                'service area': curr_node.kilometer
            })
            while curr_node and curr_node.kilometer != node_b.kilometer:
                if node_b.kilometer < curr_node.kilometer:
                    curr_node = curr_node.get_left()
                else:
                    curr_node = curr_node.get_right()
                if curr_node:
                    response.append({
                        'service area': curr_node.kilometer
                    })
                else:
                    curr_node = node_a
                    while curr_node and curr_node.kilometer != node_b.kilometer:
                        curr_node = curr_node.get_parent()
                        response.append({
                            'service area': curr_node.kilometer
                        })
        
        return Response(response)
    
    #realiza busqueda en todos los sentidos
    @action(detail=False)
    def get_route_pro(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        response = []

        return Response(response)

    #realiza búsqueda de arriba hacia abajo o de abajo hacia arriba
    @action(detail=False)
    def get_route_with_fuel_beta(self, request):
        a = request.GET.get('a')
        b = request.GET.get('b')
        number_plate = request.GET.get('number_plate')
        response = []

        node_a = ServiceArea.objects.get(kilometer=a)
        node_b = ServiceArea.objects.get(kilometer=b)
        vehicle = Vehicle.objects.get(number_plate=str(number_plate))

        curr_node = node_a
        if curr_node:
            response.append({
                'service area': curr_node.kilometer,
                'liters to load': 0
            })
            while curr_node and curr_node.kilometer != node_b.kilometer:
                before = curr_node
                if node_b.kilometer < curr_node.kilometer:
                    curr_node = curr_node.get_left()
                else:
                    curr_node = curr_node.get_right()
                if curr_node:
                    response.append({
                        'service area': curr_node.kilometer,
                        'liters to load': get_fuel(before.kilometer, before.gas_price, curr_node.kilometer, vehicle.fuel_efficiency, vehicle.fuel_tank_size)
                    })
                else:
                    curr_node = node_a
                    while curr_node and curr_node.kilometer != node_b.kilometer:
                        curr_node = curr_node.get_parent()
                        response.append({
                            'service area': curr_node.kilometer,
                            'liters to load': get_fuel(before.kilometer, before.gas_price, curr_node.kilometer, vehicle.fuel_efficiency, vehicle.fuel_tank_size)
                        })
        
        return Response(response)

def get_fuel(kilometer_a, kilometer_a_price, kilometer_b, fuel_efficiency, fuel_tank_size):
    #(? L / (kilometer_a-kilometer_b KM))= fuel_efficiency L/Km
    km = kilometer_a-kilometer_b
    if km < 0: km = km * (-1)
    l = fuel_efficiency*km
    if l > fuel_tank_size:
        l = fuel_tank_size
    return l #litros
