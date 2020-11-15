from django.urls import path
from .views import Index, Dataframes, Rate_mortality, Math_model

urlpatterns = [
    path('', Index,name="covid_index"),
    path('frames/',Dataframes, name = "frames" ),
    path('rate/<str:country_code>/', Rate_mortality, name = "rate_mortality"),
    path('model/', Math_model, name = "math_model"),
]   