from django.db import models
from django.contrib.auth.models import User

# Adds additional info that the standard User class from
# django.contrib.auth.models does not have.
#
# > We DO NOT inherit from User directly!
#
#   > That messes up the DB!
class UserProfileInfo(models.Model):

    # links up the class with User django standard class.
    # > Since we do not inherit, we need to link if this way.
    user = models.OneToOneField(User)

    # The additional fields to add to User standard model.
    # > blank means that it is not required to fill the form up.
    portfolio_site = models.URLField(blank=True)

    # IamgeField allows users to load images
    # > upload_to sends the image to 'profile_pics', the folder
    #   inside 'media' directory.
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username  # default in User() default.
