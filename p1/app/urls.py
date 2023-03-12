from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('blog_list', views.blog_list, name='blog_list'),
    #path('<int:pk>', views.blog_detail, name='blog_detail'),
    #path('create_blog_post', views.create_blog_post, name='create_blog_post'),
    path('contact', views.contact_us, name='contact_us'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
]