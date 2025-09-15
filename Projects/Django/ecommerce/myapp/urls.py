from django.urls import path,include    
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('signup/',views.signup,name='signup'),
path('login/',views.login,name='login'),
path("categories_list/", views.categories_list, name="categories_list"),
path("category_detail/", views.category_detail, name="category_detail"),
path("product_detail/", views.product_detail, name="product_detail"),
path("product/", views.product, name="products"),
path("payment/", views.payment, name="payment"),
path("payment-success/", views.payment_success, name="payment_success"),
#path('signup-verify/', views.verify_signup_otp, name='verify_signup_otp'),
]