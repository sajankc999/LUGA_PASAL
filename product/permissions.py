from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAdminUser
from .models import Product

class ProductPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return True

        
    # def has_object_permission(self, request, view, obj):
    #     # Deny actions on objects if the user is not authenticated
    #     # if not request.user.is_authenticated():
    #     #     return False
    #     if request.user.is_anonymous:
    #         return False
    #     if view.action == 'retrieve':
    #         return obj == request.user 
    #     elif view.action in ['update', 'partial_update']:
    #         return obj == request.user or request.user.is_admin
    #     elif view.action == 'destroy':
    #         return request.user.is_admin
    #     else:
    #         return False