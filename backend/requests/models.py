from django.db import models

from django.contrib.auth.models import User

class UserRequest(models.Model):
    """
    When someone has something to share
    or needs something
    this model tracks the details
    """
    requester = models.ForeignKey(User, on_delete=models.SET_NULL,
                                  blank=True, null=True)

    title = models.CharField(max_length=255)
    details = models.TextField(default='', blank=True, null=True)
    image = models.FileField(upload_to='%Y/%m/%d', null=True)
    
    # is it new? approved? completed? denied?
    # may be able to infer if completed from completed attribute
    request_status = models.CharField(default='new', max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    # any associated logged actions could trigger an update to updated
    updated = models.DateTimeField(auto_now=True)
    # when the request was completed
    completed = models.DateTimeField(blank=True, null=True)
