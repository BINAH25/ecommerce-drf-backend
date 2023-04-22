from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    #TokenRefreshView,
)
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('',views.getRoutes,name='routes'),
    path('products/',views.getProducts,name='products'),
    path('products/<str:pk>/',views.getProduct,name='products'),
    path('users/',views.getUser,name='user'),

]
