import uuid
from django.db import models
from django.conf import settings


# Create your models here.
class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

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

    def __str__(self):
        return self.name
