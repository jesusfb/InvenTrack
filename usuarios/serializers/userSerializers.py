from rest_framework import serializers
from django.contrib.auth.models import User

# Serializer para registrar un nuevo usuario
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        return user

class UserInfoRegisterSerializer(serializers.Serializer):
    rol = serializers.IntegerField()
    direccion= serializers.CharField(max_length=255)
    ciudad= serializers.CharField(max_length=100)
    pais = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=20)



# Serializer para obtener detalles del usuario autenticado
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']