from django.urls import path

from landing import views

app_name = 'landing'

urlpatterns = [
    path('index/', views.index),
    path('create/', views.post_create),
    path('read-all/', views.post_read_all),
    path('read/', views.post_read),
    path('read/<int:post_id>/', views.post_read),
    path('update/<int:post_id>/', views.post_update),
    path('delete/<int:post_id>/', views.post_delete),
    path('temptest/', views.temp_test)
]
