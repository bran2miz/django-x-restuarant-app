from django.urls import path
from .views import LocationsListView, LocationsDetailView, LocationsCreateView, LocationsUpdateView, LocationsDeleteView
from . import views
urlpatterns = [
    path('', views.locations_list, name='locations_list'),
    path('<int:pk>/', LocationsDetailView.as_view(), name='locations_detail'),
    path('create/', LocationsCreateView.as_view(), name='locations_create'),
    path('<int:pk>/update/', LocationsUpdateView.as_view(), name='locations_update'),
    path('<int:pk>/delete/', LocationsDeleteView.as_view(), name='locations_delete'),
]