from rest_framework import permissions

class PermissionAdminStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # admin only
        if request.user.id == 1:
            return True
        # prevent staff from delete except admin
        if request.method == 'DELETE' and request.user.id != 1:
            return False
        # read only
        if request.method in permissions.SAFE_METHODS:
            return True
        # permission for the writer
        if obj.writer == request.user:
            return True

