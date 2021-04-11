from django.shortcuts import render
import requests
import json
import os

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': os.environ['RAPI_KEY'],
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def covidtrackerview(request, *args, **kwaargs):
    # context = {'response':response['response'][0]}
    noofresults = int(response['results'])
    country_list = []
    for x in range(0, noofresults):
        # print(response['response'][x]['country'])
        country_list.append(response['response'][x]['country'])
    if request.method == "POST":
        selected_country = request.POST["selected_country"]
        print(selected_country)
        for x in range(0, noofresults):
            if selected_country == response['response'][x]['country']:
                active_cases = response['response'][x]['cases']['active']
                new_cases = response['response'][x]['cases']['new']
                total_cases = response['response'][x]['cases']['total']
                critical_cases = response['response'][x]['cases']['critical']
                recovered_cases = response['response'][x]['cases']['recovered']
                deaths = int(total_cases)-int(active_cases) - \
                    int(recovered_cases)
        context = {'selected_country': selected_country, 'country_list': country_list, 'new': new_cases, 'active': active_cases, 'total': total_cases,
                   'recovered': recovered_cases, 'deaths': deaths, 'critical': critical_cases}
    # print(response['response'])
        return render(request, 'index.html', context)
    for x in range(0, noofresults):
        # print(response['response'][x]['country'])
        country_list.append(response['response'][x]['country'])
    context = {'country_list': country_list}
    return render(request, 'index.html', context)
