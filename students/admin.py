from django.contrib import admin
from .models import StudentGrades, Payment, Favorite

# Register your models here.
admin.site.register(StudentGrades)
admin.site.register(Favorite)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    # This makes the columns visible in the list
    list_display = ('user', 'has_paid', 'transaction_code', 'date_paid')
    
    # Adds filters on the right side
    list_filter = ('has_paid', 'date_paid')
    
    # Allows searching by username or M-Pesa code
    search_fields = ('user__username', 'transaction_code')
