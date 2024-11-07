from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from Userauths.models import User
# Create your models here.

STATUS_CHOICES = (
  ('process', 'Processing'),
  ('shipped', 'Shipped'),
  ('delivered', 'Delivered'),
)

STATUS = (
  ('draft', 'Draft'),
  ('disabled', 'Disabled'),
  ('in_review', 'In_review'),
  ('rejected', 'Rejected'),
  ('published', 'Published')
)

RATING = (
  (1, '★'),
  (2, '★★'),
  (3, '★★★'),
  (4, '★★★★'),
  (5, '★★★★★')
)
def user_directory_path(instance,filename):
  return 'user_{0}{1}'.format(instance.user.id,filename)


  ############################################## Category ##############################################
  ############################################## Category ##############################################
  ############################################## Category ##############################################
  ############################################## Category ##############################################


class Category(models.Model):
  cid = ShortUUIDField(unique=True, max_length=20, length=10, prefix='cate', alphabet='abcdefgh123456')
  title = models.CharField(max_length=20)
  image = models.ImageField(upload_to='category')

  class Meta:
    verbose_name_plural = 'Categories'

  def category_image(self):
    return mark_safe("<img src ='%s' width='50' height='50' />"%(self.image.url))
  
  def __str__(self):
    return self.title

class Tags(models.Model):
  pass


  ############################################## Vendor ##############################################
  ############################################## Vendor ##############################################
  ############################################## Vendor ##############################################
  ############################################## Vendor ##############################################


class Vendor(models.Model):
  vid = ShortUUIDField(unique=True, max_length=20, length=10, prefix='ven', alphabet='abcdefgh123456')
  title = models.CharField(max_length=20)
  image = models.ImageField(upload_to=user_directory_path)
  descriptioh = models.TextField(null=True, blank=  True)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

  address = models.CharField(max_length=20, default="Kamalbinyak")
  contact = models.CharField(max_length=20, default= "9749341363")
  chat_res_time = models.CharField(max_length=20, default='100')
  shipping_on_time = models.CharField(max_length=100, default='100')
  authentic_rating = models.CharField(max_length=100, default='100')
  days_return = models.CharField(max_length=100, default='100')
  warrenty_peroid = models.CharField(max_length=100, default='100')
  
  class Meta:
    verbose_name_plural = 'Vendor'

  def vendor_image(self):
    return mark_safe("<img src ='%s' width='50' height='50' />"%(self.image.url))
  
  def __str__(self):
    return self.title
  

  ############################################## Products ##############################################
  ############################################## Products ##############################################
  ############################################## Products ##############################################
  ############################################## Products ##############################################

class Products(models.Model):
    pid = ShortUUIDField(unique=True, max_length=20, length=10, prefix='products', alphabet='abcdefgh123456')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(null=True, blank=True, default='This is The decription of the product')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default='1.99')
    old_price = models.DecimalField(max_digits=999999999999, decimal_places=2, default='2.99')
    specification = models.TextField(null=True, blank= True)
    # tag = models.ForeignKey(Tags,on_delete=models.SET_NULL, null=True )

    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')
    status = models.BooleanField(default = True)
    in_stock = models.BooleanField(default = True)
    featured = models.BooleanField(default = False)
    digital = models.BooleanField(default = False)

    sku = ShortUUIDField(unique=True, max_length=10, length= 1, prefix='sku', alphabet='1234567890')

    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null = True, blank=True)

    class Meta:
      verbose_name_plural = 'Products'

    def products_image(self):
      return mark_safe("<img src ='%s' width='50' height='50' />"%(self.image.url))
  
    def __str__(self):
      return self.name
    
    def get_percentage(self):
      new_price = (self.price / self.old_price) * 100
      return new_price
    
class ProductImages(models.Model):
  images = models.ImageField(upload_to='product_images', default='product.jpg')
  product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Products'


############################################## Cart Order Items ##############################################
############################################## Cart Order Items ##############################################
############################################## Cart Order Items ##############################################
############################################## Cart Order Items ##############################################
############################################## Cart Order Items ##############################################
############################################## Cart Order Items ##############################################

class CartOrder(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  price = models.DecimalField(max_digits=999999999999, decimal_places=2, default='1.99')
  paid_status = models.BooleanField(default=False)
  order_date = models.DateTimeField(auto_now_add=True)
  product_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='process')

class Meta:
    verbose_name_plural = 'Cart Order'


class CartOrderItems(models.Model):
  order = models.ForeignKey(CartOrder, on_delete=models.SET_NULL, null=True)
  invoice_number = models.CharField(max_length=200, null=True)
  product_status = models.CharField(max_length=200)
  item = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  quantity = models.IntegerField(default=0)
  price = models.DecimalField(max_digits=999999999999, decimal_places=2, default='1.99')
  total = models.DecimalField(max_digits=999999999999, decimal_places=2, default='1.99')

  class Meta:
    verbose_name_plural = 'Cart Order Items'

  def order_img(self):
      return mark_safe("<img src ='/media/%s' width='50' height='50' />"%(self.image))
  

  ############################################## Product Review ##############################################
  ############################################## Product Review ##############################################
  ############################################## Product Review ##############################################
  ############################################## Product Review ##############################################
  ############################################## Product Review ##############################################
  ############################################## Product Review ##############################################
class ProductReview(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
  review = models.TextField()
  rating = models.IntegerField(choices=RATING, default=None)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Product Review'

  
  def __str__(self):
    return self.product.name
  
  def get_rating(self):
    return self.rating
  
############################################## Product Wishlist ##############################################
############################################## Product Wishlist ##############################################
############################################## Product Wishlist ##############################################
############################################## Product Wishlist ##############################################
############################################## Product Wishlist ##############################################

class Wishlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    
  product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
  date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Wishlist'

  
  def __str__(self):
    return self.product.name
  

class Address(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=100, null=True)
  status = models.BooleanField(default=False)

  class Meta:
    verbose_name_plural = 'Address'





