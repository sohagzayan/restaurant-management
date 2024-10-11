from django.urls import path
from .views import RestaurantCreateView, RestaurantListView, LocationCreateView, LocationListView, MenuCreateView, MenuListView, CategoryListView, CategoryCreateView, MenuItemCreateView , MenuItemListView

urlpatterns = [
    path('restaurants-create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants-list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/locations-create/', LocationCreateView.as_view(), name='location-create'),
    path('restaurants/<int:restaurant_id>/locations-list/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:location_id>/menus-create/', MenuCreateView.as_view(), name='menu-create'),
    path('locations/<int:location_id>/menus-list/', MenuListView.as_view(), name='menu-list'),
    path('menus/<int:menu_id>/categories-create/', CategoryCreateView.as_view(), name='category-create'),
    path('menus/<int:menu_id>/categories-list/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/items-create/', MenuItemCreateView.as_view(), name='menuitem-create'),
    path('categories/<int:category_id>/items-list/', MenuItemListView.as_view(), name='menuitem-list'),
]