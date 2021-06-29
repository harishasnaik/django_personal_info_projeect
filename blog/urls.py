from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]