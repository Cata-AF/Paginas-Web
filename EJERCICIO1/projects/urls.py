from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name="products"),
    path('project/<str:pk>/', views.project, name="project")

]
