from django.contrib import admin
from .models import Client, Item, Order, OrderedItem

class ItemAdmin(admin.ModelAdmin):
  list_display = ('item_id', 'vendor_code', 'title', 'short_comment', 'current_price', 'reserve_amount')
  list_display_links = ('item_id', 'vendor_code', 'title')
  search_fields = ('item_id', 'vendor_code', 'title', 'current_price')

class ClientAdmin(admin.ModelAdmin):
  list_display = ('name', 'tel', 'address', 'email')
  list_display_links = ('name', 'email')
  search_fields = ('name', 'tel', 'address', 'email')

class ItemInline(admin.StackedInline):
    model = OrderedItem
    extra = 2

class OrderAdmin(admin.ModelAdmin):
  inlines = [ItemInline]
  list_display = ('order_number', 'client', 'order_price', 'delivery_method', 'order_date')
  list_display_links = ('order_number', 'client')
  filter_horizontal = ['items']
  search_fields = ('order_number', 'client', 'order_price', 'delivery_method', 'order_date')


admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
 
# Register your models here.
