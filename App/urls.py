
from django.urls import path
from App import views
app_name = 'App'
urlpatterns = [
    path('',views.HomePage, name='home' ),
    path('products/',views.Product_list_view, name='product_list' ),
    path('category/',views.Category_list_view, name='category_list' ),
]
