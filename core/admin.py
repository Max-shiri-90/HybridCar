from django.contrib import admin
from .models import User, Car, Part


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ordering = 'name',
    list_display = ('name', 'model', 'is_repaired', 'is_finished')
    list_filter = ('is_repaired', 'is_finished')
    list_editable = ('is_repaired', 'is_finished')
    actions = ('enable_is_repaired', 'enable_is_finished', 'disabled_is_required', 'disabled_is_finished')

    def query_set(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(user=request.user).all()

    def enable_is_repaired(self, request, query_set):
        for car in query_set:
            car.is_repaired = True
            car.save()

    def enable_is_finished(self, request, query_set):
        for car in query_set:
            car.is_finished = True
            car.save()

    def disabled_is_required(self, request, query_set):
        for car in query_set:
            car.is_required = True
            car.save()

    def disabled_is_finished(self, request, query_set):
        for car in query_set:
            car.is_finished = True
            car.save()

admin.site.register(User)
admin.site.register(Part)
