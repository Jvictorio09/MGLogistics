from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

def home_alt(request):
    return render(request, 'myapp/home_alt.html')

def about(request):
    return render(request, 'myapp/about.html')

def projects(request):
    return render(request, 'myapp/projects.html')

def pricing(request):
    return render(request, 'myapp/pricing.html')

def team(request):
    return render(request, 'myapp/team.html')

def faq(request):
    return render(request, 'myapp/faq.html')

# views.py
from django.shortcuts import render
from .models import Service

def services_list_view(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'myapp/services.html', {'services': services})


# myapp/views.py
from django.shortcuts import render, get_object_or_404
from .models import Service

def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    all_services = Service.objects.filter(is_active=True)
    return render(request, 'myapp/service_detail.html', {
        'service': service,
        'all_services': all_services
    })


from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'myapp/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.views += 1
    blog.save()
    return render(request, 'myapp/blog_detail.html', {'blog': blog})


def contact(request):
    return render(request, 'myapp/contact.html')
