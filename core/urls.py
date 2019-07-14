from django.urls import path

from . import views

urlpatterns = [
    path('encode/', views.EncodeView.as_view(), name='encode'),
    path('decode/', views.DecodeView.as_view(), name='decode')
]
