from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import UserSerializer,EditorSerializer
from .models import CustomUser
from .permissions import IsLocalOwner
from django.shortcuts import get_object_or_404
from .models import EDITOR_GROUP
from django.contrib.auth.models import Group
# Create your views here.

@api_view(['POST'])
def SignupUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"signup successfull","user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsLocalOwner])
def UserList(request):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

 #assign editor group for specific user
@api_view(['POST'])
@permission_classes([IsLocalOwner])
def assign_editor_group(request, id,):
    user = get_object_or_404(CustomUser, id=id)
    is_approved = request.data.get("is_approved", False)
    user.is_approved = is_approved
    user.save()
    if is_approved:
        editor_group = Group.objects.get(name=EDITOR_GROUP)
        user.groups.add(editor_group)

    return Response({
        "message": f"User {user.username} {'approved and added to Editor group'}"
    }, status=status.HTTP_200_OK)
    
#list editors
@api_view(['GET'])
@permission_classes([IsLocalOwner])
def list_editor(request):
    editors = CustomUser.objects.filter(groups__name="Editor")
    data = [{"id":user.id, "username":user.username}for user in editors]
    return Response({"editors":data})