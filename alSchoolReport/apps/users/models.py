from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser




# 因为分层设计的需要，应该将其放置在最底层，供其他层使用和调用
# default=datetime.now  为啥不是# default=datetime.now（）
# #这个样子的话，每次编译前就会被执行，而不是增加后才会执行
class BaseModel(models.Model):
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    # create_time = models.DateField(auto_now=True)
    # 确认不会被新建一张表
    class Meta:
        abstract = True

