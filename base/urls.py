from django.urls import path
from .views import hello, logout_view, home


urlpatterns = [
    path('', home),
    path('hello/', hello),
    path('logout/', logout_view)
]