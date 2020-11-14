from django.urls import path
from .views import Index, Dataframes, Rate_mortality

urlpatterns = [
    path('', Index,name="covid_index"),
    path('frames/',Dataframes, name = "frames" ),
    path('rate/', Rate_mortality, name = "rate_mortality"),
]