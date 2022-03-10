from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Restaurant


class RestaurantsListView(ListView):
    template_name = "restaurants/restaurants-list.html"
    model = Restaurant


class RestaurantsDetailView(DetailView):
    template_name = "restaurants/restaurants-detail.html"
    model = Restaurant


class RestaurantsCreateView(CreateView):
    template_name = "restaurants/restaurants-create.html"
    model = Restaurant
    fields = ['name', 'description', 'foodie']


class RestaurantsUpdateView(UpdateView):
    template_name = "restaurants/restaurants-update.html"
    model = Restaurant
    fields = ['name', 'description', 'foodie']


class RestaurantsDeleteView(DeleteView):
    template_name = "restaurants/restaurants-delete.html"
    model = Restaurant
    success_url = reverse_lazy("restaurants_list")