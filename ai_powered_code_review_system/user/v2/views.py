from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from user.models import User
from user.v2.serializers import UserRegistrationSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# class LoginAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data = data)
#             if serializer.is_valid():
#                 email = serializer.validated_data['email']
#                 password = serializer.validated_data['password']
                
#                 user = authenticate(email = email, password = password)
#                 if user is None:
#                     return Response({
#                         'status' : 400,
#                         'message' : 'Invalid Password',
#                         'data' : {}
#                     })
#                 refresh = RefreshToken.for_user(user)

#                 return {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 }
     
                
#             return Response({
#                 'status' : 400,
#                 'message' : 'Invalid credentials',
#                 'data' : serializer.errors
#             })
            
#         except Exception as e:
#             print(e)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserProfileSerializer

    def get_permissions(self):
        if self.action in ['register', 'login', 'create']: 
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': UserProfileSerializer(user).data,
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return Response({
                'user': UserProfileSerializer(user).data,
                'message': 'Login successful'
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})

    @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
