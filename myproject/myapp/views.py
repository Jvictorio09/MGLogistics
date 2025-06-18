from django.shortcuts import render


def home(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'myapp/index.html', {'services': services})

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


from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

def send_quote(request):
    if request.method == 'POST':
        first = request.POST.get('firstn')
        last = request.POST.get('lastn')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        New Quote Request:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}
        Subject: {subject}

        Message:
        {message}
        """

        send_mail(
            subject=f"Quote Request: {subject}",
            message=full_message,
            from_email='juliavictorio16@gmail.com',
            recipient_list=['juliavictorio16@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Quote sent successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponseRedirect('/')
