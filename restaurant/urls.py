from django.urls import path
from .views import RestaurantListCreateView, LocationListCreateView, MenuListCreateView, CategoryListCreateView, MenuItemListCreateView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:restaurant_id>/locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:location_id>/menus/', MenuListCreateView.as_view(), name='menu-list-create'),
    path('menus/<int:menu_id>/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:category_id>/items/', MenuItemListCreateView.as_view(), name='menuitem-list-create'),
]