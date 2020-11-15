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

def Rate_mortality(request, country_code):

    #country = "Ecuador"
    rate = process.Process()
    rate.get_country_stats(country_code)
    #print(rate._country_stats)
    #print(rate.get_new_cases())

    mean_cases, std_cases = rate.get_new_cases()
    mean_deaths, std_deaths = rate.get_new_deaths()
    #print(mean_cases, std_cases)
    #print(mean_deaths, std_deaths)

    print(rate._get_power_of_x_variables())

    rate_value = rate.mortality_rate(mean_deaths,mean_cases)

    

    #return HttpResponse("mortality rate in the country "+country+", is: "+ str("{0:.2f}".format(rate_value)) + "%")

    return JsonResponse({'country':country_code,'rate_mortality': rate_value})

def Math_model(request):
    # 1 instantiate the Math model class 
    # 2 put the values to fetch model, and 
    #   can get the prediction 

    return HttpResponse("")

