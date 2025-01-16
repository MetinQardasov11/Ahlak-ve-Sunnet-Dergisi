from django.shortcuts import render, redirect
from contact.models import Address, Email, Phone
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        print(contact_form)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Mesajınız başarıyla gönderildi!")
            return redirect('contact:contact')
        else:
            messages.error(request, "Formda hatalar var, lütfen kontrol edin.")
    else:
        contact_form = ContactForm()

    
    addresses = Address.objects.all()
    emails = Email.objects.all()
    phones = Phone.objects.all()
    
    context = {
        'addresses': addresses,
        'emails': emails,
        'phones': phones,
        'form' : contact_form
    }
    
    return render(request, 'contact/contact.html', context)