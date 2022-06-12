from rest_framework.permissions import IsAuthenticated


class IsReception(IsAuthenticated):
    def has_permission(slef, request, view):
        return super().has_permission(request, view) and request.user.role == "reception"

class IsAdmin(IsAuthenticated):
    def has_permission(slef, request, view):
        return super().has_permission(request, view) and request.user.role == "admin"

class IsTechnician(IsAuthenticated):
    def has_permission(slef, request, view):
        return super().has_permission(request, view) and request.user.role == "technician"

class IsInspector(IsAuthenticated):
    def has_permission(slef, request, view):
        return super().has_permission(request, view) and request.user.role == "inspector"
