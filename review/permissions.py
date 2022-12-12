from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            # если просто чтегия
            return True
        if not request.user.is_authenticated:
            # если юзера нет
            return False
            

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

