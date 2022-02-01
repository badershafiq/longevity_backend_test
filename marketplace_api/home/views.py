from django.shortcuts import render


def marketplace_home(request):
    return render(request, 'home/index.html', {})

def recommendation_api(request):
    instance = Recommendation.objects.get()
    instance.getRecommendation()
    response = requests.get('https://bmiheatlhtracker.com/json/')
    apidata = response.json()
    recommendation = instance.getRecommendation(apidata)

    return render(request, 'home/recommendation.html', {
        'recommendation': recommendation
    })

