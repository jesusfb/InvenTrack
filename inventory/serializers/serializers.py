from rest_framework import serializers


class InventoryDataClassSerializer(serializers.Serializer):
    producto = serializers.CharField()
    cantidad = serializers.CharField()
    bodega = serializers.CharField()


class CreateInventorySerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    cantidad = serializers.CharField()
    bodega = serializers.CharField()


