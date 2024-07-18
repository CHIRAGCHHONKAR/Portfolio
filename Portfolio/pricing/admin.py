from django.contrib import admin
from django.utils.html import format_html

from Portfolio.pricing.models import *

class PriceAdmin(admin.ModelAdmin):
    list_display = ('plan_logo', 'plan_name', 'price', 'display_services', 'purchase')

    def display_services(self, obj):
        services = obj.services.split(',')
        formatted_services = []
        
        for service in services:
            is_new = '##' in service
            parts = service.split('~~')
            
            formatted_service = parts[0].replace('##', '').strip()
            
            if len(parts) > 1:
                formatted_service += f' <del>{parts[1].strip()}</del>'
            
            if is_new:
                formatted_service += ' <span class="badge badge-success">new</span>'
            
            formatted_services.append(formatted_service)
        
        return format_html('<br>'.join(formatted_services))

    display_services.short_description = 'Services'

admin.site.register(Price, PriceAdmin)