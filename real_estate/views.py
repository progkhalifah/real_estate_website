from django.shortcuts import render
import logging

from real_estate.models import *

# Create your views here.
logger = logging.getLogger('real_estate')


def home(request):
    logger.debug('Performing operation...')
    get_all_property_listing = TblPropertyListing.objects.all()
    get_city_property = TblPropertyCity.objects.all()
    get_type_property = TblTypeProperty.objects.all()
    context = {
        'all_property_listing': get_all_property_listing,
        'all_property_city': get_city_property,
        'all_property_type': get_type_property,
    }
    return render(request, 'real_estate/main/home.html', context)


def get_single_property(request, uuid_property):
    get_one_property = TblPropertyListing.objects.get(id=uuid_property)
    get_all_images_property = TblPropertyImages.objects.filter(property_title__id=uuid_property)

    context = {
        'getOneProperty': get_one_property,
        'getAllImagesProperty': get_all_images_property,
    }

    return render(request, 'real_estate/main/one_property.html', context)


def custom_404(request, excption):
    return render(request, 'real_estate/page_not_found/404.html', status=404)


def custom_500(request):
    return render(request, 'real_estate/page_not_found/404.html')
