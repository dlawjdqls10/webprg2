from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
# Article이라는 클래스를 만들어서 admin에 등록해 주세요
# Create a class named Article and register the table into admin
# Article테이블에는 title, body, author, create_date필드가 포함되어 있습니다.
# title, body, author, create_date are included in the Article table.
# 함수를 이용하여 각각의 title이 article을 나타내주는 이름이 되게 하고, article-detail을 위한 url도 생성합니다.


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    author = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

