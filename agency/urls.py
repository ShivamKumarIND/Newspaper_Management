from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.home, name='home'),
    path('start-newspaper/', views.start_newspaper, name='start_newspaper'),
    path('close-newspaper/', views.close_newspaper, name='close_newspaper'),
    path('payment-details/', views.payment_details, name='payment_details'),
    path('register-complaint/', views.register_complaint, name='register_complaint'),
    path('join-distributor/', views.join_distributor, name='join_distributor'),
    path('newspaper-sold/', views.newspaper_sold, name='newspaper_sold'),
]
