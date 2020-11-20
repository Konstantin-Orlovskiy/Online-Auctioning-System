from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class Item(models.Model):  # Class of items which are created by users
    # An item identifier is assigned to any object automatically
    title = models.CharField(max_length=250)  # item title
    condition = models.CharField(max_length=250, choices=(('new', 'New'), ('used', 'Used'),),
                                 default='new'
                                 )  # The condition of the item, predefined choices
    description = models.CharField(max_length=250)  # The item description
    end_date = models.DateTimeField(blank=False)  # The auction expiration time to be set by User
    user = models.ForeignKey(get_user_model(), default=User, on_delete=models.CASCADE)  # Information about the item owner
    timestamp = models.DateTimeField(auto_now_add=True)  # The time of item registration in the system


class Auction(models.Model):  # Class of auctions which are accessible to view by users
    # An item identifier is assigned to any object automatically
    item = models.CharField(max_length=250)  # Item for sale
    time_left = models.DurationField()  # The time left to complete
    auction_status = models.CharField(max_length=250,
                                      choices=(('open', 'Open'), ('completed', 'Completed'),),
                                      default='new'
                                      )  # An action status e.g. open for offers or completed

class Bid(models.Model):  # Class of bids where users make their bids and see the bids history.
    auction = models.CharField(max_length=250)  # Reference to the auction
    bidding_price = models.FloatField()  # Bidding price
    user = models.CharField(max_length=250)  # Information about the bidder
    timestamp = models.DateTimeField(auto_now_add=True)  # The time of making the bid
