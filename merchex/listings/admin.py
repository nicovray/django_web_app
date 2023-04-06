from django.contrib import admin

from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title','year','band','sold','type') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)