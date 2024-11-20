from django.shortcuts import render
from .models import Slider, Featured, About, Info, Sections, Service, Part, Action, Title, Portfolio, Team, Staff, Contact

# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    featured = Featured.objects.all()
    about = About.objects.first()
    info = Info.objects.all()
    sections = Sections.objects.all()
    service = Service.objects.first()
    parts = Part.objects.all()
    action = Action.objects.first()
    title = Title.objects.first()
    portfolio = Portfolio.objects.all()
    team = Team.objects.first()
    staff = Staff.objects.all()
    contact = Contact.objects.first()

    context = {
        'sliders': sliders,
        'featured': featured,
        'about': about,
        'info': info,
        'sections': sections,
        'service':service,
        'parts':parts,
        'action':action,
        'title': title,
        'portfolio':portfolio,
        'team':team,
        'staff':staff,
        'contact':contact
    }
    return render (request,'index.html', context)

def portfolio(request):
    return render(request,'portfolio-details.html')

def service(request):
    return render(request,'service-details')

def starter(request):
    return render(request, 'starter-page.html')