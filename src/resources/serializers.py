from rest_framework import serializers
from .models import Item, Auction, Bid


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'condition', 'description', 'end_date', 'user')

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('item', 'auction_status', 'time_left')

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('auction', 'bidding_price', 'timestamp')
