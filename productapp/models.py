from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)                  # 상품 이름
    price = models.IntegerField(default=0)                  # 상품 가격
    market_name = models.CharField(max_length=30, blank=True)
    head_image = models.ImageField(upload_to='productapp/images/%Y/%m/%d/', blank=True)
    # writer : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/product/{self.pk}'