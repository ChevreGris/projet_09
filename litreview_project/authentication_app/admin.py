import imp
from django.contrib import admin

from authentication_app.models import User
from litreview_app.models import Ticket

admin.site.register(User)
admin.site.register(Ticket)