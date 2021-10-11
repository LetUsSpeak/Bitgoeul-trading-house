from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=32, verbose_name="사용자명")
    id = models.CharField(max_length=32, primary_key=True, verbose_name="id")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    address = models.CharField(max_length=5, verbose_name="사용자 지역")
    token = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username        # 문자열 반환

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'




