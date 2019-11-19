from django.contrib import admin
from basic_app.models import UserProfileInfo

admin.site.register(UserProfileInfo)

# we do not need to register User() default form since it comes
# with the default admin site in Django itself.
