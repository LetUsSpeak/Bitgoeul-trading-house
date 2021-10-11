from django.db import models

REGION_CHOICE = [
    ('서울특별시', '서울특별시'),
    ('대전광역시', '대전광역시'),
    ('대구광역시', '대구광역시'),
    ('울산광역시', '울산광역시'),
    ('광주광역시', '광주광역시'),
    ('인천광역시', '인천광역시'),
    ('부산광역시', '부산광역시'),
    ('경기도', '경기도'),
    ('강원도', '강원도'),
    ('충청도', '충청도'),
    ('경상도', '경상도'),
    ('전라도', '전라도'),
    ('제주도', '제주도')

]
# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=32, verbose_name="사용자명")
    id = models.CharField(max_length=32, primary_key=True, verbose_name="id")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    address = models.CharField(choices=REGION_CHOICE, max_length=5, verbose_name="사용자 지역")
    token = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username        # 문자열 반환

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'




