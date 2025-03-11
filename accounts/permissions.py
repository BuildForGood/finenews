from rest_framework import permissions

class IsLocalOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Local News Owner").exists()

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Editor").exists()
