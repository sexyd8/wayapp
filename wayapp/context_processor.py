from .models import  *

    

def cartread(request):
    cart=Shopcart.objects.filter(user__username=request.user.username, paid_order=False)


    cartreader=0
    for item in cart:
        cartreader += item.quantity

    context={
        'cartreader':cartreader
    }
    return context

def dropdown(request):
    categories = Category.objects.all()

    context = {
        'categories':categories
    }

    return context
    


def member(request):
    member = Member.objects.all()

    context = {
        'member':member
    }

    return context



# def upgrade(request):
#     upgrade = Member.objects.exclude(title='Wood')

#     context = {
#         'upgrade':upgrade
#     }

#     return context


# def downgrade(request):
#     downgrade = Member.objects.exclude(title='Diamond')

#     context = {
#         'downgrade':downgrade
#     }

#     return context
