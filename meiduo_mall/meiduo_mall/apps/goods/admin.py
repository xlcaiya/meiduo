from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.GoodsCategory)  # 商品类别
admin.site.register(models.GoodsChannel)  # 商品频道
admin.site.register(models.Goods)  # 商品SPU
admin.site.register(models.Brand)  # 品牌
admin.site.register(models.GoodsSpecification)  # 商品规格
admin.site.register(models.SpecificationOption)  # 规格选项
admin.site.register(models.SKU)  # 商品SKU
admin.site.register(models.SKUSpecification)  # SKU具体规格
admin.site.register(models.SKUImage)  # SKU图片
