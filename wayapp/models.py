from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', default='pix.jpg')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', default='pix.jpg')
    price = models.FloatField(default=10.00)
    description = models.TextField()
    local = models.BooleanField()
    foreign = models.BooleanField()
    latest = models.BooleanField()
    wood=models.BooleanField(default=False)
    gold=models.BooleanField(default=False)
    diamond=models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Shopcart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    basket_no=models.CharField(max_length=36)
    quantity=models.IntegerField()
    paid_order=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Carousel(models.Model):
    image =models.ImageField(upload_to='carouselpix',default='carousel.jpg')
    comment=models.CharField(max_length=100)


    def __str__(self):
        return self.comment

class Payment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.IntegerField()
    basket_no=models.CharField(max_length=36)
    pay_code=models.CharField(max_length=36)
    paid_order=models.BooleanField(default=False)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Member(models.Model):
    title = models.CharField(max_length=50)
    fee = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'member'
        managed = True
        verbose_name = 'Member'
        verbose_name_plural = 'Member'





class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, blank=True, null=True)
    address=models.CharField(max_length=100,  blank=True, null=True)
    fee=models.FloatField()
    member=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,  blank=True, null=True)
    email=models.EmailField()
   

    def __str__(self):
        return self.first_name



class Membership(models.Model):
    Profile=models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    membership=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    fee = models.FloatField()
    pay_code=models.CharField(max_length=36)
    memeber_no=models.CharField(max_length=36)
   

    def __str__(self):
        return self.first_name

