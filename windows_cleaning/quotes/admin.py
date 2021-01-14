from django.contrib import admin
from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'submitted', 'quote_date', 'quote_price', 'priority')
    list_filter = ('submitted', 'quote_date')
    readonly_fields = ('submitted',)
    fieldsets = (
        ('Basic Information', {
            'classes': ('wide',),
            'fields': ('name', 'email', 'description')
        }),
        ('Contact details', {
            'classes': ('collapse', 'wide'),
            'fields': ('position', 'company', 'phone', 'address', 'web')
        }),
        ('Job information', {
            'classes': ('extra_wide',),
            'fields': ('site_status', 'priority', 'job_file', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('quote_date', 'quote_price', 'user_name')
        }),
    )

admin.site.register(Quote, QuoteAdmin)