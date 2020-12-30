from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('front/' , include("front.urls")),
    path('front/' , include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
