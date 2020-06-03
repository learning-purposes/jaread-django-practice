from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # will return true if the user is admin
        # or the http verb is among get,head,option
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin