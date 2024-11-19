from django.shortcuts import render
from .models import Slider, Featured, About, Info, Sections, Service

# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    featured = Featured.objects.all()
    about = About.objects.first()
    info = Info.objects.all()
    sections = Sections.objects.all()
    services = Service.objects.first()

    context = {
        'sliders': sliders,
        'featured': featured,
        'about': about,
        'info': info,
        'sections': sections,
        'services':services
    }
    return render (request,'index.html', context)

def portfolio(request):
    return render(request,'portfolio-details.html')

def service(request):
    return render(request,'service-details')

def starter(request):
    return render(request, 'starter-page.html')