from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.userSerializers import UserRegisterSerializer, UserSerializer, UserInfoRegisterSerializer, RolSerielizers
from .interface_adapters.controllers.userController import ControlUsers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Registro de nuevos usuarios
@api_view(['POST'])
def register_user(request):
    control = ControlUsers()
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            serializeruser = UserInfoRegisterSerializer(data=request.data)
            print(user.id)

            rol = int(serializer.validated_data["rol"])
            direccion = serializer.validated_data["direccion"]
            ciudad = serializer.validated_data["ciudad"]
            pais = serializer.validated_data["pais"]
            telefono = serializer.validated_data["telefono"]
            usuario_instance =control.create_register_user(rol, direccion, ciudad, pais, telefono, user.id)


        return Response({
            "message": "Usuario creado con éxito",
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para generar tokens JWT
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"message": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create_rol(request):
    control = ControlUsers()
    pass


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_roles(request):
    control = ControlUsers()
    try:
        roles = control.get_roles()

        print(roles)

        serializer = RolSerielizers(roles, many= True)
        return Response(serializer.data)

    except Exception as e:
        return Response({'error':"no hay registros"}, status=404)


@api_view(["GET"])
def get_byid_user(request, user_id):
    control  = ControlUsers()
    try:

        usuario = control.get_user_byid(user_id)
        serializer = UserSerializer(usuario,  many= False)  # Asumiendo que tienes un UserSerializer
        return Response(serializer.data)  # Devuelve los datos serializados

    except Exception as e:
        return Response({'error': f"No hay registros {e}"}, status= 500)


@api_view(["GET"])
def get_all_users(request):
    control = ControlUsers()
    try:
        usuarios = control.get_users()
        serializer = UserSerializer(usuarios, many= True)  # Asumiendo que tienes un UserSerializer
        return Response(serializer.data)  # Devuelve los datos serializados

    except Exception as e:
        return Response({'error': f"not fount {e}"}, status= 500)


    

