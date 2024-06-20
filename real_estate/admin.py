from django.contrib import admin

from real_estate.models import *


# Register your models here.

@admin.register(TblTypeProperty)
class TblTypePropertyAdmin(admin.ModelAdmin):
    list_display = ('name_type_property',)
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(TblPropertyFor)
class TblPropertyForAdmin(admin.ModelAdmin):
    list_display = ('property_for', )
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(TblPropertyCountry)
class TblPropertyCountryAdmin(admin.ModelAdmin):
    list_display = ('property_country', )
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(TblPropertyCity)
class TblPropertyCityAdmin(admin.ModelAdmin):
    list_display = ('property_city', )
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(TblPropertyListing)
class TblPropertyListingAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'property_for', 'country_property', 'city_property', 'location_property', 'price_property', 'size_property', 'beds_property', 'bath_property', )
    list_filter = ('property_type', 'property_for', 'country_property', 'city_property',)
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    search_fields = ('location_property',)
    # ordering = ('', )


@admin.register(TblPropertyImages)
class TblPropertyImagesAdmin(admin.ModelAdmin):
    list_display = ('property_title', 'images_property')
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
