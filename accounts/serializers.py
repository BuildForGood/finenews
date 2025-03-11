from accounts.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','username','email','password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class EditorSerializer (serializers.ModelSerializer):
    class Meta:
        model:CustomUser
        fields = ['id','is_approved']