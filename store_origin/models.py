import random, string
from django.db import models

class Item(models.Model):
    
    def generate_code():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    
    item_id = models.AutoField(primary_key=True, verbose_name = 'ID товара')
    vendor_code = models.CharField(default = generate_code, max_length=20,
                                   unique = True, verbose_name='Артикул')
    title = models.CharField(max_length=50, verbose_name='Название')
    short_comment = models.TextField(max_length=100, verbose_name='Краткое описание')
    full_comment = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Полное описание')
    base_price = models.FloatField(verbose_name='Базовая цена')
    current_price = models.FloatField(verbose_name='Текущая цена')
    reserve_amount = models.IntegerField(verbose_name='Запас на складе')
    min_num = models.IntegerField(null=True, blank=True,  verbose_name='Минимальное количество')
    
    def __str__(self):
        return f'{self.title} {self.current_price}'
    
    class Meta():
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-item_id']

    
class Client(models.Model):

    name = models.CharField(max_length=100,  verbose_name='Имя')
    tel = models.CharField(max_length = 20,  verbose_name='Телефон')
    address = models.TextField(max_length = 1000, null=True, blank=True,  verbose_name='Адрес')
    email = models.CharField(max_length = 100,  verbose_name='Электронная почта')
    
    def __str__(self):
        return f'{self.name} {self.tel}'
    
    class Meta():
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'

    
class Order(models.Model):


    def get_total_price(self):
        total_sum = 0
        for i in self.ordereditem_set.all():
            total_sum = total_sum + i.item.current_price *i.count
        return total_sum
      
    client = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name='Клиент')
    order_number = models.AutoField(primary_key=True, verbose_name = 'Номер заказа')
    Payment_Method_Choices = (
                                ('Онлайн оплата', 'Онлайн оплата'),
                                ('Картой курьеру', 'Картой курьеру'),
                                ('Наличными', 'Наличными'),
    )
    payment_method = models.CharField(choices = Payment_Method_Choices,
                                      max_length = 20, verbose_name = 'Метод оплаты')
    delivery_method_choices = (
                                ('Курьером', 'Курьером'),
                                ('Самовывоз', 'Самовывоз'),
                                ('Почта России', 'Почта России'),
                                ('Доставка CDEK', 'Доставка CDEK'),
    )
    delivery_method = models.CharField(choices = delivery_method_choices,
                                       max_length = 20, verbose_name = 'Метод доставки')
    items = models.ManyToManyField('Item', verbose_name='Товар', through='OrderedItem')
    order_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата заказа')
    order_price = models.FloatField(verbose_name='Стоимость заказа')
    #order_price_1 = property(get_total_price)
    #models.CharField(default = get_total_price, max_length=20,
     #                              blank = True, verbose_name='Стоимость заказа 1')
    
    def __str__(self):
        return f'Заказ {self.order_number}'

    class Meta():
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-order_date']
        
class OrderedItem(models.Model):

    item = models.ForeignKey(Item, on_delete=models.PROTECT,)
    order = models.ForeignKey(Order, on_delete=models.PROTECT,)
    count = models.IntegerField()
    
    
    def total(self):
        return self.count * self.item.current_price

    def __str__(self):
        return f"{self.item.title}, " \
               f"{self.item.current_price} * {self.count} = {self.total()}"
    
