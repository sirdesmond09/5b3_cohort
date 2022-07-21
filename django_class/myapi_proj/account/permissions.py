from rest_framework import permissions


class IsAdminOrSignUp(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == 'POST':
            return True

        if request.user.is_authenticated:
            return request.user.is_staff or request.user.is_superuser
        return False 