# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    birth = models.DateTimeField(blank=True, null=True, default=timezone.now)
    interest = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Country(models.Model):

    #__Country_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Country_FIELDS__END

    class Meta:
        verbose_name        = _("Country")
        verbose_name_plural = _("Country")


class Language(models.Model):

    #__Language_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Language_FIELDS__END

    class Meta:
        verbose_name        = _("Language")
        verbose_name_plural = _("Language")


class Currency(models.Model):

    #__Currency_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    symbol = models.TextField(max_length=255, null=True, blank=True)

    #__Currency_FIELDS__END

    class Meta:
        verbose_name        = _("Currency")
        verbose_name_plural = _("Currency")


class Institution(models.Model):

    #__Institution_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)

    #__Institution_FIELDS__END

    class Meta:
        verbose_name        = _("Institution")
        verbose_name_plural = _("Institution")


class Track(models.Model):

    #__Track_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Track_FIELDS__END

    class Meta:
        verbose_name        = _("Track")
        verbose_name_plural = _("Track")


class Publish_Period(models.Model):

    #__Publish_Period_FIELDS__
    month = models.TextField(max_length=255, null=True, blank=True)

    #__Publish_Period_FIELDS__END

    class Meta:
        verbose_name        = _("Publish_Period")
        verbose_name_plural = _("Publish_Period")


class Col_Style(models.Model):

    #__Col_Style_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)

    #__Col_Style_FIELDS__END

    class Meta:
        verbose_name        = _("Col_Style")
        verbose_name_plural = _("Col_Style")


class Rank(models.Model):

    #__Rank_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    desc = models.TextField(max_length=255, null=True, blank=True)

    #__Rank_FIELDS__END

    class Meta:
        verbose_name        = _("Rank")
        verbose_name_plural = _("Rank")


class Journal(models.Model):

    #__Journal_FIELDS__
    institution = models.ForeignKey(institution, on_delete=models.CASCADE)
    cover = models.CharField(max_length=255, null=True, blank=True)
    rank = models.ForeignKey(rank, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    publish_period = models.ForeignKey(publish_period, on_delete=models.CASCADE)
    currency = models.ForeignKey(currency, on_delete=models.CASCADE)
    apc = models.IntegerField(null=True, blank=True)
    rating_avg = models.IntegerField(null=True, blank=True)
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    contact = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    col_style = models.ForeignKey(col_style, on_delete=models.CASCADE)
    last_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Journal_FIELDS__END

    class Meta:
        verbose_name        = _("Journal")
        verbose_name_plural = _("Journal")



#__MODELS__END
