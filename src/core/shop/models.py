import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


MONTH_CHOICES = (
    ("Хасс", "Хасс"),
    ("Фуэрте", "Фуэрте"),
    ("1", "1"),
    ("2", "2"),
)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller_profile")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="buyer_profile")
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Buyer {self.user.username}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="subcategories", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PropertyKey(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Название свойства, например, 'Цвет', 'Размер'.")

    def __str__(self):
        return self.name


class PropertyValue(models.Model):
    key = models.ForeignKey(PropertyKey, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100, help_text="Значение свойства, например, 'Красный', 'XL'.")

    def __str__(self):
        return f"{self.key.name}: {self.value}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    photo = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    article = models.CharField(max_length=100, unique=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    properties = models.ManyToManyField(PropertyValue, related_name="products")  # Используем связь ManyToMany
    property_key = models.CharField(max_length=255, choices=MONTH_CHOICES)
    property_key_2 = models.CharField(max_length=255, choices=MONTH_CHOICES)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()  # Оценка от 1 до 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'buyer']

    def __str__(self):
        return f"Review of {self.product.name} by {self.buyer.user.username}"




class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name="orders")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')],
        default='pending'
    )

    def __str__(self):
        return f"Order {self.id} by {self.buyer.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
