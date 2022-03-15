import imp
from django.contrib import admin

from authentication_app.models import User
from litreview_app.models import Ticket, Review

admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Review)