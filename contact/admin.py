from django.contrib import admin
from .models import Contact, Address, Email, Phone

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_reply', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'address',)
    
    
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('title', 'email',)
    
    
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone',)
    