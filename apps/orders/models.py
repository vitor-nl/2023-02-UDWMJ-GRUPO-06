from django.db import models
from products.models import Product
from clients.models import Client

# Create your models here.

class Order(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    
    @property
    def total_price(self):
        itens = self.orderitem_set.all()

        if itens.exists():
            valor_final = sum(item.valor_dos_produtos() for item in itens)
            return valor_final
        else:
            return 0,0
            
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']
        managed = True
        db_table = 'orders'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.FloatField('Preço unitario',null=True, blank=True,default=0)

    def valor_dos_produtos(self):
        valor = (self.quantity)*(self.unitary_price)
        return valor

    class Meta:
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']