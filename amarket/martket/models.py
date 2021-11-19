from django.db import models

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=50)
    p_price = models.CharField(max_length=8)
    p_cout = models.IntegerField()
    
    def __str__(self):
        return self.p_name
    
    # @staticmethod
    # def make_order(pid):
    #     product = Product.objects.filter(id = pid)
    #     product.p_cout -= 1
    #     product.save()
         