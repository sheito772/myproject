from django.shortcuts import render
from .models import Score, RankingUser
from .serializers import ScoreSerialzer, UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = RankingUser.objects.all()
    serializer_class = UserSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.select_related('user').order_by('-score')
    serializer_class = ScoreSerialzer