from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=100,unique=100)
    slug=models.SlugField(max_length=100,unique=True)

    def _get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='product')
    stock=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)

