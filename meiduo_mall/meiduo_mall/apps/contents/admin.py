from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.ContentCategory)  # 广告内容类别
admin.site.register(models.Content)  # 广告内容
