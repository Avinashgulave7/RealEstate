from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .forms import CustomAuthForm
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.contrib import admin


from . import views

urlpatterns=[
    path('',views.index),
    path('property_details/<id>/',views.Property_Details),
    path('property_details_rent/<id>/',views.Property_Details_Rent),
    path('property_details_land/<id>/',views.Property_Details_Land),
    path('about/',views.About),
    path('buy/',views.Buy_Page),
    path('rent/',views.Rent_Page),
    path('Property_Land/',views.Land_Page),
    path('contact/',views.Contact_page),
    path('add_property/',views.Add_Property),
    path('add_buy/',views.Add_Buy),
    path('add_rent/',views.Add_rent),
    path('add_land/',views.Add_land),
    path('login1/',views.Login),
    path('signup/',views.SignUp),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=CustomAuthForm)),
    path('accounts/',include("django.contrib.auth.urls")),
    path('logout/',views.Logout),
    path('user_buy_viewall/<id>/',views.User_Buy_Viewall),
    path('update_user_prop/<id>/',views.Update_Buy),
    path('user_buy_delete/<id>/',views.User_Buy_delete),
    path('user_rent_viewall/<id>/',views.User_Rent_Viewall),
    path('update_user_prop_rent/<id>/',views.Update_Rent),
    path('user_rent_delete/<id>/',views.User_Rent_delete),
    path('update_user_prop_land/<id>/', views.Update_Land),
    path('user_land_viewall/<id>/', views.User_Land_Viewall),
    path('user_land_delete/<id>/', views.User_Land_delete),
    path('property/',views.Property),
    path('price_sort_low_to_high/',views.Price_Low_To_High),
    path('price_sort_high_to_low/',views.Price_High_To_Low),
    path('area_sort_low_to_high/',views.Area_Low_To_High),
    path('area_sort_high_to_low/',views.Area_High_To_Low),
    path('buy_price_sort_low_to_high/', views.Buy_Price_Low_To_High),
    path('buy_price_sort_high_to_low/', views.Buy_Price_High_To_Low),
    path('buy_area_sort_low_to_high/', views.Buy_Area_Low_To_High),
    path('buy_area_sort_high_to_low/', views.Buy_Area_High_To_Low),
    path('rent_price_sort_low_to_high/', views.Rent_Price_Low_To_High),
    path('rent_price_sort_high_to_low/', views.Rent_Price_High_To_Low),
    path('rent_area_sort_low_to_high/', views.Rent_Area_Low_To_High),
    path('rent_area_sort_high_to_low/', views.Rent_Area_High_To_Low),
    path('land_price_sort_low_to_high/', views.Land_Price_Low_To_High),
    path('land_price_sort_high_to_low/', views.Land_Price_High_To_Low),
    path('land_area_sort_low_to_high/', views.Land_Area_Low_To_High),
    path('land_area_sort_high_to_low/', views.Land_Area_High_To_Low),

    path('email/<id>/',views.Send_Email,name='email'),





            ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

