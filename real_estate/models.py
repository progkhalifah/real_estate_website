import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class TblCustomUser(AbstractUser):
    phone_number = models.IntegerField(verbose_name=_('Phone Number')),

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class TblTypeProperty(models.Model):
    name_type_property = models.CharField(verbose_name=_('Name Type Property'), max_length=250)

    def __str__(self):
        return self.name_type_property

    class Meta:
        verbose_name = _('Type Property')
        verbose_name_plural = _('Types Properties')


class TblPropertyFor(models.Model):
    property_for = models.CharField(verbose_name=_('Property For'), max_length=250)

    def __str__(self):
        return self.property_for

    class Meta:
        verbose_name = _('Property For')
        verbose_name_plural = _('Properties For')


class TblPropertyCountry(models.Model):
    property_country = models.CharField(verbose_name=_('Property Country'), max_length=250)

    def __str__(self):
        return self.property_country

    class Meta:
        verbose_name = _('Property Country')
        verbose_name_plural = _('Properties Country')


class TblPropertyCity(models.Model):
    property_city = models.CharField(verbose_name=_('Property City'), max_length=250)

    def __str__(self):
        return self.property_city

    class Meta:
        verbose_name = _('Property City')
        verbose_name_plural = _('Properties City')


class TblPropertyListing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title_property = models.CharField(verbose_name=_('Title Property'), max_length=250)
    image_property = models.ImageField(upload_to="images/property_listing", verbose_name=_('Image Property'))
    location_property = models.TextField()
    country_property = models.OneToOneField(TblPropertyCountry, on_delete=models.CASCADE, verbose_name=_("Country Property"),)
    city_property = models.OneToOneField(TblPropertyCity, on_delete=models.CASCADE, verbose_name=_("City Property"),)
    property_type = models.OneToOneField(TblTypeProperty, on_delete=models.CASCADE, verbose_name=_("Property Type"))
    property_for = models.ForeignKey(TblPropertyFor, on_delete=models.CASCADE, verbose_name=_("Property For"))
    size_property = models.IntegerField(verbose_name=_("Size Property"))
    beds_property = models.IntegerField(verbose_name=_("Beds Property"))
    bath_property = models.IntegerField(verbose_name=_("Bath Property"))
    price_property = models.DecimalField(verbose_name=_("Price Property"), max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title_property

    class Meta:
        verbose_name = _('Property Listing')
        verbose_name_plural = _('Properties Listing')


class TblPropertyImages(models.Model):
    property_title = models.ForeignKey(TblPropertyListing, related_name='images', on_delete=models.CASCADE)
    images_property = models.FileField(upload_to="images/property_listing", verbose_name=_('Images Property'))

    class Meta:
        verbose_name = _('Property Image')
        verbose_name_plural = _('Properties Images')











