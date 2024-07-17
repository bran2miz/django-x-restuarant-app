from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Location

def locations_list(request):
    locations = list(Location.objects.values())
    return JsonResponse(locations, safe=False)

class LocationsListView(ListView):
    template_name = "locations/locations-list.html"
    model = Location


class LocationsDetailView(DetailView):
    template_name = "locations/locations-detail.html"
    model = Location


class LocationsCreateView(CreateView):
    template_name = "locations/locations-create.html"
    model = Location
    fields = ['location', 'description', 'traveler']


class LocationsUpdateView(UpdateView):
    template_name = "locations/locations-update.html"
    model = Location
    fields = ['location', 'description', 'traveler']


class LocationsDeleteView(DeleteView):
    template_name = "locations/locations-delete.html"
    model = Location
    success_url = reverse_lazy("locations_list")