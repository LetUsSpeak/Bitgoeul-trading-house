from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=30)                  # 상품 이름
    price = models.IntegerField(default=0)                  # 상품 가격
    market_name = models.CharField(max_length=30, blank=True)
    head_image = models.ImageField(upload_to='productapp/images/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # writer : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/product/{self.pk}'


