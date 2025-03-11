from django.urls import path,include
from .views import SignupUser, UserList,assign_editor_group,list_editor
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignupUser),
    path("editor/<int:id>/", assign_editor_group, name="user-detail"),
    path("listeditor/",list_editor),
    path('userslist/', UserList),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]