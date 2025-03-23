from accounts.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    groups = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['id','username','email','first_name','last_name','password','groups']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def get_groups(self, obj):
        return [group.name for group in obj.groups.all()]


class EditorSerializer (serializers.ModelSerializer):
    class Meta:
        model:CustomUser
        fields = ['id','is_approved']