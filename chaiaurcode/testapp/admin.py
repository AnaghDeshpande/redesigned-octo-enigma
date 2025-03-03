from django.contrib import admin
from .models import ChaiVariety, chaiReview, ChaiCertificate, Store

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extras = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
   list_display = ('name', 'location')
   filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')

# Register your models here.
admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)