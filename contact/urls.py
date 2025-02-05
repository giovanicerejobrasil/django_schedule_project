# type: ignore
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/edit/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # User (CRUD)
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
