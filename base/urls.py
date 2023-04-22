from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    #TokenRefreshView,
)
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('',views.getRoutes,name='routes'),
    path('products/',views.getProducts,name='products'),
    path('products/<str:pk>/',views.getProduct,name='products'),
    
    path('getAllUser/',views.getAllUser,name='getAllUser'),
    path('user/',views.getUser,name='user'),
    path('user/register/',views.registerUser,name='user-register'),

]
