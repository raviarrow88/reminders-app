from .views import reminder_page

from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.reminder_page, name="reminder_home_page"),

]