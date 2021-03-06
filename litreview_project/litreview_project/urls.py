"""litreview_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication_app.views
import litreview_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication_app.views.login_page, name='login'),
    path('logout/', authentication_app.views.logout_user, name='logout'),
    path('signup', authentication_app.views.signup_page, name='signup'),
    path('tickets/add/', litreview_app.views.ticket_create, name='ticket_create'),
    path('tickets/<int:id>/add/review', litreview_app.views.ticket_add_review, name='ticket_add_review'),
    path('tickets/<int:id>/change/', litreview_app.views.ticket_update, name='ticket_update'),
    path('tickets/<int:id>/delete/', litreview_app.views.ticket_delete, name='ticket_delete'),
    path('review/add/', litreview_app.views.review_create, name='review_create'),
    path('review/<int:id>/change/', litreview_app.views.review_update, name='review_update'),
    path('review/<int:id>/delete/', litreview_app.views.review_delete, name='review_delete'),
    path('user/', litreview_app.views.user_post, name='user_post'),
    path('user/social/', litreview_app.views.sub, name='user_social'),
    path('user/social/<int:id>/delete/', litreview_app.views.sub_delete, name='sub_delete'),
    path('flux/', litreview_app.views.flux, name='flux'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
