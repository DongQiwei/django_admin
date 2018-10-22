from django.db import models


class Shop(models.Model):
    shop_id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField('名称', max_length=32, unique=True)
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)
    title = models.CharField('标题', max_length=255, db_index=True)

    class Meta:
        db_table = 'shop00'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
