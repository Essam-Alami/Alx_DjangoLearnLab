from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owner (author) can edit/delete; others read-only.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only requests are allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the object's author
        return obj.author == request.user
