from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('data/',views.mydata,name='data'),
    path('date/',views.date),
    path('rendertemp/',views.rendertemp),
    path('temperature/',views.temperature,name='temperature'),
    path('renderqr/',views.renderqr),
    path('qrcode1/',views.qrcode1,name='qrcode1'),
    path('rendercontact/',views.rendercontact,name='rendercontact'),
    path('contactus/',views.contactus1,name='contactus'),
    path('renderlogin/',views.renderlogin,name='renderlogin'),
    path('renderregister/',views.renderregister,name='renderregister'),
    path('login/',views.login,name='login'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('renderbuy/',views.renderbuy,name='renderbuy'),
    path('buy/',views.buy,name='buy'),
    path('about/',views.about,name='about'),
    path('renderfeedback/',views.renderfeedback,name='renderfeedback'),
    path('index/',views.index,name='index'),
    path('/logout',views.logout,name='logout'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('users/',views.users,name='users'),
    path('contactdetails/',views.contactreviews,name='contactdetails'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('items/',views.items,name='items'),
    path('additem/',views.additem,name='additem'),
    path('biodata/',views.biodata,name='biodata'),
    path('checkout/',views.checkout,name='checkout'),

]
