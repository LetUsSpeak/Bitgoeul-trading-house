from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)                  # 상품 이름
    price = models.IntegerField(default=0)                  # 상품 가격
    content = models.TextField()                            # 상품 설명
    upload_date = models.DateTimeField(auto_now_add=True)    # 상품 게시일
    # writer : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.name}'