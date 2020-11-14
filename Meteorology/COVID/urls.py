from django.urls import path
from .views import Index, Dataframes

urlpatterns = [
    path('', Index,name="covid_index"),
    path('frames/',Dataframes, name = "frames" ),
]