from django.urls import path
from .import views
urlpatterns = [
    path('',views.load_first_page,name='load_first_page'),
    path('load_second_page',views.load_second_page,name='load_second_page'),
]
