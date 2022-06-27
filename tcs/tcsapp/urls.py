from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('welcome/', views.welcome),
    path('creating/', csrf_exempt(views.Creating.as_view())),
    path('fetch/', csrf_exempt(views.Fetch.as_view())),
    path('ac_fetch/', csrf_exempt(views.Ac_Fetch.as_view())),
    # path('ac_city/', csrf_exempt(views.Ac_city.as_view())),

]