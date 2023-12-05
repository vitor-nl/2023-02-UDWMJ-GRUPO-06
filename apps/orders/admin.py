from django.contrib import admin
from .models import Order
from .models import OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):  # Pode ser TabularInline ou StackedInline
    model = OrderItem
    extra = 0  # Especifica quantos formulários em branco serão exibidos

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    readonly_fields = ('exibir_total_price',)  # Adicione o campo somente leitura

    def exibir_total_price(self, Order):
        return Order.total_price  # Usar o método total_price do modelo Order
    exibir_total_price.short_description = 'Preço total'  # Nome do campo no admin

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)