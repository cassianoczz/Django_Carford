from carford_app import views
from django.urls import path

app_name = 'carford_app'

urlpatterns = [
    # Owner
    path('', views.OwnerList.as_view(), name='owner_list'),
    path('owner/detail/<int:pk>/', views.OwnerDetailView.as_view(), name='owner_detail'),
    path('owner/create/', views.OwnerCreateView.as_view(), name='owner_create'),
    path('owner/update/<int:pk>/', views.OwnerUpdateView.as_view(), name='owner_update'),
    path('owner/delete/<int:pk>/', views.OwnerDeleteView.as_view(), name='owner_delete'),

    # Cars
    path('car/create/<int:pk>/', views.CarCreateView.as_view(), name='car_create'),
    path('car/update/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
    path('car/delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),
]
