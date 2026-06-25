from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.contrib import messages
from products.models import Product
from testimonials.models import Testimonial

from django.core.mail import send_mail
from django.conf import settings


def home(request):

    featured_products = Product.objects.filter(
        is_featured=True
    )[:3]

    testimonials = Testimonial.objects.filter(
        is_active=True
    )[:3]

    context = {
        'featured_products': featured_products,
        'testimonials': testimonials,
    }

    return render(
        request,
        'core/home.html',
        context
    )
def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            send_mail(
                subject=f"New Contact Message: {contact.subject}",
                message=f"""
        Name: {contact.name}
        Email: {contact.email}
        Phone: {contact.phone}

        Message:
        {contact.message}
        """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(
                request,
                'Your message has been sent successfully.'
            )

            return redirect('contact')

    else:

        form = ContactForm()

    return render(
        request,
        'core/contact.html',
        {'form': form}
    )

def about(request):
    return render(request, 'core/about.html')
