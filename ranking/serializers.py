from rest_framework import serializers
from .models import Score, RankingUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingUser
        fields = '__all__'

class ScoreSerialzer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source='user.name')
    class Meta:
        model = Score
        fields = ('id', 'score', 'created_at', 'user', 'username')