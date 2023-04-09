from django.urls import path

from . import views

app_name = "BaseApp"

urlpatterns = [
    path('', views.index, name="home"),
    # path('test', views.test, name='test'),
    path('upload/', views.upload_file, name='upload'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('intersection/<int:intersection_id>/', views.intersection, name='intersection'),
    path('intersection/<int:intersection_id>/edit', views.edit, name='edit'),
]
