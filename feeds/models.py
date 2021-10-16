# feeds/models.py
from django.db import models
from django.utils import timezone
from faker import Faker

# Create your models here.
class Feed(models.Model): # 모델 클래스명은 단수형을 사용 (Posts(x) Post(O))
    # id는 자동 추가
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.content

    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            Feed.objects.create(content=myfake.catch_phrase())