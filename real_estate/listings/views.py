from django.shortcuts import render
from .models import Listing
from .forms import ListingForm

# Create your views here.
def listing_list(request):
  listings = Listing.objects.all()
  context = {
    "listings": listings
  }
  return render(request, "listings.html", context)

def listing_retrieve(request, id):
  listing = Listing.objects.get(id=id)
  context = {
    "listing": listing
  }
  return render(request, "listing.html", context)

def listing_create(request):
  form = ListingForm()
  context = {
    "form": form
  }
  return render(request, "ListingForm.html", context)