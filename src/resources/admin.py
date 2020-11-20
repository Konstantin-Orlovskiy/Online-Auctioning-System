from django.contrib import admin
from .models import Item, Auction, Bid


# Register your models here.
admin.site.register(Item)
admin.site.register(Auction)
admin.site.register(Bid)
