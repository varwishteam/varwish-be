import uuid
from django.db import models


# Create your models here.
class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    EMPTY = 'em'
    OPEN = 'op'
    COMPLETED = 'co'
    CLOSED = 'cl'

    WISHLIST_STATUS = (
        (EMPTY, 'Empty'),
        (OPEN, 'Open'),
        (COMPLETED, 'Completed'),
        (CLOSED, 'Closed')
    )

    status = models.CharField(
        max_length=2,
        choices=WISHLIST_STATUS,
        default=EMPTY
    )