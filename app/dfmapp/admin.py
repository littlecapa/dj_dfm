from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Config, LichessConfigModel

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Config.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        config = Config.objects.first()
        if config:
            return HttpResponseRedirect(reverse('admin:dfmapp_config_change', args=[config.pk]))
        return super().changelist_view(request, extra_context)

@admin.register(LichessConfigModel)   
class LichessConfigModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if LichessConfigModel.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        config = LichessConfigModel.objects.first()
        if config:
            return HttpResponseRedirect(reverse('admin:dfmapp_lichessconfigmodel_change', args=[config.pk]))
        return super().changelist_view(request, extra_context)
