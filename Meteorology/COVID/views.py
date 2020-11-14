from django.shortcuts import render
from .Process import Process as process
from django.http import HttpResponse, JsonResponse

# Create your views here.


def Index(request):
    
    new_process = process.Process()

    return JsonResponse({'keys': str(new_process.get_keys())})


def Dataframes(request):

    datas = process.Process()
    print(datas.Read())

    return HttpResponse(str(datas.Read()))

def Rate_mortality(request):

    country = "Ecuador"
    rate = process.Process()
    rate.get_country_stats(country)
    
    

    return HttpResponse("mortality rate in the country"+country+", is: ",)