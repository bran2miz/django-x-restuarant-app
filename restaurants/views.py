from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Restaurant
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

def restaurants_list(request):
    if request.method == 'GET':
        restaurants = list(Restaurant.objects.values())
        return JsonResponse(restaurants, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        restaurant = Restaurant.objects.create(
            name=data['name'],
            description=data['description'],
            foodie_id=data['foodie']
        )
        return JsonResponse({
            'id': restaurant.id,
            'name': restaurant.name,
            'description': restaurant.description,
            'foodie': restaurant.foodie_id
        })

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
