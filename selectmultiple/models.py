from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Meal(MPTTModel):
    name = models.CharField(max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class MealLink(models.Model):
    meals = models.ManyToManyField(Meal, blank=True, default=None)
    checkbox_input = models.CharField(max_length=50, null=True, blank=True)


