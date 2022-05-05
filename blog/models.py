from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)  #짧은 내용
    content=models.TextField()  #긴 내용

    created_at=models.DateTimeField(auto_now_add=True) #현재시간 작성
    updated_at = models.DateTimeField(auto_now=True) #수정된 시간만 수정
    #author:추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'