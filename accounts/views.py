from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserShowSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import EmailConfirmation , User
from django.core.mail import send_mail
from django.conf import settings
from .utils import send_confirmation_email



class UserRegisterView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            user = srz_data.create(srz_data.validated_data)
            send_confirmation_email(user)
            return Response({'detail' : 'Verification email sent.'}, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors , status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmailView(APIView):
    def get(self, request , key):
        try:
            confirmation = EmailConfirmation.objects.filter(key=key).last()
            if confirmation.confirm():
                return Response({'detail' : 'Email confirmed. You can now log in.'} , status=status.HTTP_200_OK)
            return Response({'detail' : 'Invalid or expired key.'} , status=status.HTTP_400_BAD_REQUEST)
        except EmailConfirmation.DoesNotExist:
            return Response({'detail' : 'Invalid key.'} , status=status.HTTP_400_BAD_REQUEST)


class ShowUsersView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        users = User.objects.all()
        serializer = UserShowSerializer(users, many=True)
        return Response(serializer.data)