from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.conf import settings  # 导入Django的配置（用SECRET_KEY生成Token）
import jwt  # 导入jwt库
import datetime  # 处理Token过期时间

from .models import User, Company
from .serializers import UserSerializer, CompanySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': '注册成功'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def login(self, request):
        # 1. 验证账号密码
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if not user:
            # 账号密码错误
            return Response({'msg': '账号密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # 2. 生成Token（有效期1天）
        payload = {
            'user_id': user.id,  # 存用户ID
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # 过期时间
            'iat': datetime.datetime.utcnow()  # 生成时间
        }
        # 用Django的SECRET_KEY加密生成Token
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        
        # 3. 返回Token和用户信息
        return Response({
            'msg': '登录成功',
            'user': user.username,
            'token': token  # 关键：返回Token
        }, status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer