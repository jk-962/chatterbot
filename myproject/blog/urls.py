from django.urls import path
from .import views 


urlpatterns=[
    path('',views.index,name='index'),
    path('spec/',views.spec,name='spec'),
    path('getResponse',views.getResponse,name='getResponse')
]