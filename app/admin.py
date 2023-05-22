from django.contrib import admin
from app.models import Customer, Product, Cart, OrderedPlaced
from django.utils.html import format_html
from django.urls import reverse


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode']    
    
@admin.register(Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']
    
@admin.register(Cart)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    
@admin.register(OrderedPlaced)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'ordered_date', 'status']
    
    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    
    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)