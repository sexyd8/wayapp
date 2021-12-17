from django.contrib import admin
from . models import Category, Payment, Product,  Carousel , Shopcart , Membership,Profile, Member

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','category','name','image','price','description','foreign','latest','local','wood','gold','diamond')
    

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image','comment')

class ShopcartAdmin(admin.ModelAdmin):
    list_display = ('id','user','product','basket_no','quantity','paid_order')


class PaymentAdmin(admin.ModelAdmin):
    list_display=('id','user','amount','basket_no','first_name','last_name','phone','address','city','state')


class MemberAdmin(admin.ModelAdmin):
    list_display=('id','title','fee')
    

class MembershipAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','membership','phone','fee','pay_code',)
  

class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','first_name','last_name','phone','fee','member','address','gender','email')




admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Shopcart,ShopcartAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Membership,MembershipAdmin)
admin.site.register(Profile,ProfileAdmin)
