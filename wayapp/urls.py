from django.urls import path
from .  import views




urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('diamond/', views.diamond, name='diamond'),
    path('gold/', views.gold, name='gold'),
    path('wood/', views.wood, name='wood'),
    path('products/', views.products, name='products'),
    path('details/<str:id>/', views.details, name='details'),
    path('login/', views.loginform, name='loginform'),
    path('membership/<int:id>/', views.membership, name='membership'),
    path('memberfee/', views.memberfee, name='memberfee'),
    path('signup/',views.signupform, name='signupform'),
    path('password/',views.password, name='password'),
    path('logoutform/',views.logoutfunc, name='logoutfunc'),
    path('profile/',views.profile, name='profile'),
    path('profile-update/',views.profileupdate, name='update'),
    path('confirmation/',views.confirmation, name='confirmation'),
    path('upgrade/<str:id>/',views.upgrade, name='upgrade'),
    path('downgrade/<str:id>/',views.downgrade, name='downgrade'),
    path('memberupgrade/',views.memberupgrade, name='memberupgrade'),
    path('memberdowngrade/',views.memberdowngrade, name='memberdowngrade'),
]
