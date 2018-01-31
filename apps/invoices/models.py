import uuid
from django.db import models


class DefaultBaseModel(models.Model):
    slug = models.SlugField(max_length=36, unique=True, null=False, blank=False)

    def save(self, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4()

        super().save(**kwargs)

    class Meta:
        abstract = True


class TextFile(DefaultBaseModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return "{} - {}".format(self.slug, self.file.name)

    class Meta:
        ordering = ['slug']


class Invoice(DefaultBaseModel):
    slug = models.SlugField(max_length=36, unique=True, null=False, blank=False)
    purchaser_name = models.CharField(max_length=255, blank=False, null=False)
    item_description = models.CharField(max_length=255, blank=False, null=False)
    item_price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    purchase_count = models.IntegerField(blank=False, null=False)
    merchant_address = models.CharField(max_length=255, blank=False, null=False)
    merchant_name = models.CharField(max_length=255, blank=False, null=False)
    text_file = models.ForeignKey(TextFile, related_name='invoices', on_delete=models.CASCADE, to_field='slug',
                                  db_column='text_file_slug', verbose_name='text_file_slug')

    def __str__(self):
        return "{} - {}".format(self.purchaser_name, self.item_description)

    class Meta:
        ordering = ('purchaser_name',)
        verbose_name_plural = 'invoices'

