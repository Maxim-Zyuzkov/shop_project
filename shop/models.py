from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.CharField(max_length=100, verbose_name="Страна")
    description = models.TextField(blank=True, verbose_name="Описание")
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Производители"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    product_image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Фото товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Цена")
    stock = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Количество на складе")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products', verbose_name="Производитель")
    def __str__(self): return self.name
    class Meta: verbose_name_plural = "Товары"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self): return f"Корзина {self.user.username}"
    def total_price(self): return sum(item.item_price() for item in self.items.all())
    class Meta: verbose_name_plural = "Корзины"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    def __str__(self): return f"{self.product.name} ({self.quantity} шт.)"
    def item_price(self): return self.product.price * self.quantity
    def clean(self):
        if self.quantity > self.product.stock:
            raise ValidationError(f"На складе всего {self.product.stock} шт.")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    class Meta: verbose_name_plural = "Элементы корзины"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=250, verbose_name="Адрес доставки")
    city = models.CharField(max_length=100, verbose_name="Город")
    postal_code = models.CharField(max_length=20, verbose_name="Почтовый индекс")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")
    def __str__(self): return f"Заказ #{self.id}"
    def total_cost(self): return sum(item.cost() for item in self.items.all())
    class Meta: verbose_name_plural = "Заказы"; ordering = ['-created']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    def __str__(self): return f"{self.product.name} x {self.quantity}"
    def cost(self): return self.price * self.quantity
    class Meta: verbose_name_plural = "Элементы заказа"

# ==========================================
# МОДЕЛЬ ПРОФИЛЯ (ЗАДАНИЕ 1)
# ==========================================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, verbose_name="Полное имя")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=250, blank=True, verbose_name="Адрес")
    city = models.CharField(max_length=100, blank=True, verbose_name="Город доставки")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="Почтовый индекс")
    favorite_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Любимая категория")
    clothing_size = models.CharField(max_length=10, blank=True, verbose_name="Размер одежды", choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')])
    def __str__(self): return f"Профиль {self.user.username}"
    class Meta: verbose_name_plural = "Профили"