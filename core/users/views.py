from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from .models import Profile, User
from .serializers import UserSerializer
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.
class RegisterUserAPiVIew(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    serializer = UserSerializer

    def post(self, request):
        user = authenticate(request.data)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({
                'user': user.username,
                'token': token.key
            })
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutAPIview(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ProfileCreateList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUDD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
