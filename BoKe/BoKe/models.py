from django.db import models


class Comments(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=20,default='匿名')
    content = models.CharField(verbose_name='内容',max_length=200)
    create_time = models.DateTimeField(verbose_name='时间',auto_now_add=True)


    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]