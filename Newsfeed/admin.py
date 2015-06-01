from django.contrib import admin
from Newsfeed.models import admin_login, comment

admin.site.register(comment)
admin.site.register(admin_login)

