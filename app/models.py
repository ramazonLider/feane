from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    meal = models.ManyToManyField('Meal', related_name="meals", blank=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField('Category', related_name="categories")
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='meals/')

    def __str__(self):
        return self.name
