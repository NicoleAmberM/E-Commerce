from app.serializers.auth_serializer import LoginSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            auth_header = request.META["HTTP_AUTHORIZATION"]
            access_token = auth_header.split()[1]

            untyped_token = UntypedToken(token=access_token)
            untyped_token.set_exp(0)

            return Response(
                {"detail": "Successfully logged out."}, status=status.HTTP_200_OK
            )
        except InvalidToken:
            return Response(
                {"detail": "Invalid access token."}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {"detail": "Error occurred during logout."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
