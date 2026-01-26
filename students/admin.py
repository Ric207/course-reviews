from django.contrib import admin
from .models import StudentGrades, Payment, Favorite

# Register your models here.
admin.site.register(StudentGrades)
admin.site.register(Favorite)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    # What columns to show
    list_display = ('user', 'transaction_code', 'has_paid', 'date_paid')
    
    # Filters on the right side
    list_filter = ('has_paid', 'date_paid')
    
    # Search box functionality
    search_fields = ('user__username', 'transaction_code')
    
    # THIS IS THE MAGIC LINE:
    # It allows you to check/uncheck 'Has Paid' directly in the list view
    list_editable = ('has_paid',)
