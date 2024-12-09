from django.urls import path
from . import views 

urlpatterns = [
    path('',views.viewData),
    path('add/',views.postData),
]
