from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import serializers
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.http import Http404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .interfaceAdapter.controller.inventoryControl import ControlIventory

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 
# from vulnerabilities.interface_adapters.dependencies import openapidoc

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from inventory.interfaceAdapter.dependencies.logs import logger, logs_register
# Configuración del logger


notfound_message = "No hay registros de inventario"


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all(request):
    logger = logs_register('inventory_logs')
    control = ControlIventory()
    try:
        inventory = control.get_all_inventory()
        print(inventory)
        serializer = serializers.InventoryDataClassSerializer(inventory, many=True)
        logger.info(f"Solicitud exitosa a la ruta /api/get-all-inventory {request.headers}")
        return Response(serializer.data)
    except Http404:
        # Loguear error cuando no se encuentra inventario
        logger.error(notfound_message)
        raise NotFound(notfound_message)

    except Exception as e:
        # Loguear cualquier otra excepción que ocurra
        logger.error(f"Error inesperado: {str(e)}")
        return Response({"error": "Error interno del servidor"}, status=500)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_byid(request, id):
    control = ControlIventory()
    try:
        inventory = control.get_byid_inventory(id)
        
        serializer = serializers.InventoryDataClassSerializer(inventory, many=False)
        # logger.info("Solicitud a la ruta /vulnerabilities.\n")
        return Response(serializer.data)
    except Exception as e:
        # Capturar cualquier excepción y registrar su mensaje
        return Response({"error": str(e)}, status=404)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_inventory(request):
    # Serializa los datos entrantes
    control = ControlIventory()
    serializer = serializers.InventoryDataClassSerializer(data=request.data)

    # Valida los datos
    if serializer.is_valid():
        # Obtener la instancia del producto por el id
        
        # Procesa los datos si son válidos
        producto = int(serializer.validated_data["producto"])
        cantidad = serializer.validated_data["cantidad"]
        bodega = serializer.validated_data["bodega"]
        inventory_instance = control.create_register_inventory(producto, cantidad, bodega)
        fixed_serializer = serializers.InventoryDataClassSerializer(inventory_instance)
        return Response(fixed_serializer.data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)